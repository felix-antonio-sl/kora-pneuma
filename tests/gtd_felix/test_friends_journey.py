"""FARO synthetic journey: real service/store, scripted meaning, fake Telegram HTTP.

No Hermes inference is exercised. Owner/principal commands below are explicit
screenplay decisions, not language understanding attributed to the runtime.
run_journey() keeps all state in a temporary directory and returns evidence only.
"""
import copy
import hashlib
import tempfile
import unittest
from pathlib import Path

from test_telegram import (
    AiohttpTelegramClient, FakeHTTP, GTDService, TelegramAdapter, TelegramConfig, message,
)


INPUTS = (
    'Quiero volver a juntarme con mis amigos. Lo pienso, pasan las semanas y queda en nada.',
    'Más íntimo. Estoy pensando en dos personas, no en el grupo entero.',
    'Sí. Pero ahora déjalo descansar.',
    'Aquello de ver a mis amigos…',
)
DRAFTS = (
    'Hola, hace tiempo que no nos juntamos y me gustaría volver a verlos. '
    '¿Les tinca que conversemos para organizar algo?',
    'Hola, me gustaría que nos juntáramos a conversar con calma, tú y yo. '
    '¿Te tinca? Si te dan ganas, podemos ver cuándo nos acomoda.',
)


async def run_journey():
    """Return actual fake-HTTP transcript, service receipts and acceptance checks."""
    with tempfile.TemporaryDirectory(prefix='gtd-friends-') as directory:
        root = Path(directory)
        service = GTDService(root)
        http = FakeHTTP()
        config = TelegramConfig('synthetic-friends-bot', 7, 9, 'felix')
        adapter = TelegramAdapter(service, AiohttpTelegramClient('synthetic-secret', http, attempts=1), config)
        phases, decisions, checks = [], [], {}
        captures, saved_before_ack = [], []
        sent_offset = call_offset = 0

        def on_send(payload):
            if payload['text'].startswith('Guardado.'):
                saved_before_ack.append(any(
                    (root / item['original']['path']).read_text() == item['text']
                    for item in service.query() if item['text'] == INPUTS[len(saved_before_ack)]))
        http.on_send = on_send

        def phase(name):
            nonlocal sent_offset, call_offset
            phases.append({'phase': name, 'http_calls': copy.deepcopy(http.calls[call_offset:]),
                           'telegram_outputs': copy.deepcopy(http.sent[sent_offset:]),
                           'items': copy.deepcopy(service.query())})
            sent_offset, call_offset = len(http.sent), len(http.calls)

        async def receive(index):
            http.updates.append(message(index + 1, INPUTS[index]))
            await adapter.poll_once()
            await adapter.process_pending()
            item = next(i for i in service.query() if i['text'] == INPUTS[index])
            captures.append(copy.deepcopy(item))
            return item

        def execute(actor, action, item, fields, label):
            command = {'operation_id': 'friends-' + label, 'action': action,
                       'item_id': item['id'], 'expected_version': item['version'], 'fields': fields}
            receipt = service.execute(actor, command)
            decisions.append({'screenplay_decision': label, 'actor': actor,
                              'command': command, 'receipt': copy.deepcopy(receipt)})
            return receipt

        def applied(receipt):
            if receipt['status'] != 'applied':
                raise AssertionError(receipt)
            return receipt['item']

        def route(capture, subject, label):
            return execute('gtd-felix', 'clarify', capture, {
                'destination': 'existing', 'target_item_id': subject['id'],
                'reason': 'El guion identifica este mensaje como continuación del mismo asunto.',
                'intent_basis': {'quote': capture['text'], 'source_item_id': capture['id']},
            }, label)

        try:
            subject = await receive(0)
            checks['capture_before_interpretation'] = subject['kind'] == 'capture' and not subject.get('materials')
            phase('1_original_saved_before_scripted_interpretation')
            subject = applied(execute('gtd-felix', 'clarify', subject, {
                'kind': 'possibility', 'commitment': 'proposed',
                'title': 'Volver a juntarme con mis amigos',
            }, 'interpret-possibility'))
            authority = service.authorize('gtd-felix', 'prepare_private', subject['id'])
            checks['existing_private_authority'] = authority == {
                'allowed': True, 'reason': 'standing_private_preparation'}
            subject = applied(execute('gtd-felix', 'put_material', subject, {
                'content': DRAFTS[0], 'title': 'Borrador privado grupal, sin enviar',
            }, 'private-draft-v1'))
            material_id = subject['materials'][0]['id']
            phase('1_private_group_draft_prepared_not_delivered')

            correction = await receive(1)
            applied(route(correction, subject, 'link-correction'))
            # Interpretation remains scripted, but the configured principal uses
            # the real direct human source instead of impersonating the owner.
            subject = applied(execute('gtd-felix', 'apply_human_instruction', subject, {
                'instruction': 'correct',
                'intent_basis': {'source_item_id': correction['id'],
                    'source_revision': len(correction['source_revisions']),
                    'quote': correction['source_revisions'][-1]['text']},
                'changes': {'title': 'Volver a ver a dos amigos, de forma más íntima',
                    'text': INPUTS[0] + '\nCorrección: ' + INPUTS[1]},
            }, 'apply-human-correction'))
            checks['old_draft_invalid_after_correction'] = not service.materials(subject['id'])[0]['valid']
            await adapter.show_result(subject['id'])
            checks['old_draft_never_delivered'] = not any(DRAFTS[0] in p['text'] for p in http.sent)
            subject = applied(execute('gtd-felix', 'put_material', subject, {
                'material_id': material_id, 'content': DRAFTS[1],
                'title': 'Borrador privado personal, reutilizable por separado; sin enviar',
                'source_versions': {correction['id']: len(correction['source_revisions'])},
            }, 'private-draft-v2'))
            await adapter.show_item(subject)
            await adapter.show_result(subject['id'])
            phase('2_correction_linked_and_personal_draft_returned')

            pause_input = await receive(2)
            applied(route(pause_input, subject, 'link-rest'))
            pause_receipt = execute('gtd-felix', 'apply_human_instruction', subject, {
                'instruction': 'pause', 'changes': {},
                'intent_basis': {'source_item_id': pause_input['id'],
                    'source_revision': len(pause_input['source_revisions']),
                    'quote': pause_input['source_revisions'][-1]['text']},
            }, 'pause-subject-without-date')
            subject = service.get_item(subject['id'])
            checks['subject_really_paused'] = pause_receipt['status'] == 'applied' and subject['status'] == 'paused'
            paused_authority = service.authorize('gtd-felix', 'prepare_private', subject['id'])
            # Shared authorization also serves reads/routing; probe the write boundary below.
            paused_write = {'status': 'NOT_RUN', 'reason': 'subject_pause_not_applied'}
            if checks['subject_really_paused']:
                before_attempt = copy.deepcopy(subject)
                paused_write = execute('gtd-felix', 'put_material', subject, {
                    'material_id': material_id, 'content': 'Preparación que debe ser rechazada durante el descanso.',
                }, 'reject-preparation-during-rest')
                checks['paused_write_rejected_without_new_version'] = (
                    paused_write['status'] == 'rejected'
                    and service.get_item(subject['id']) == before_attempt)
            else:
                checks['paused_write_rejected_without_new_version'] = False
            checks['rest_suspends_preparation'] = checks['paused_write_rejected_without_new_version']
            phase('3_rest_requested_subject_pause_probe')

            before_restart = copy.deepcopy(subject)
            previous_service, previous_adapter = service, adapter
            service.close()
            service = GTDService(root)
            adapter = TelegramAdapter(service, AiohttpTelegramClient('synthetic-secret', http, attempts=1), config)
            checks['real_store_and_adapter_restart'] = (service is not previous_service and adapter is not previous_adapter
                                                       and service.get_item(subject['id']) == before_restart)
            returned = await receive(3)
            return_route = route(returned, subject, 'link-explicit-return')
            checks['return_linked_to_same_subject'] = return_route['status'] == 'applied'
            before_read = copy.deepcopy(service.get_item(subject['id']))
            await adapter.show_item(before_read)
            # Exercise the existing user callback over fake HTTP, including its
            # persisted opaque token, instead of calling the result reader alone.
            button = next(b for row in http.sent[-1]['reply_markup']['inline_keyboard']
                          for b in row if b['text'] == 'Ver resultado')
            http.updates.append({'update_id': 5, 'callback_query': {
                'id': 'friends-explicit-result', 'from': {'id': 7},
                'message': {'chat': {'id': 9}}, 'data': button['callback_data']}})
            await adapter.poll_once()
            await adapter.process_pending()
            after_read = service.get_item(subject['id'])
            checks['explicit_read_does_not_reactivate_or_mutate'] = after_read == before_read
            checks['return_preserves_rest'] = after_read['status'] == 'paused'
            return_text = '\n'.join(p['text'] for p in http.sent[sent_offset:])
            checks['return_recovers_corrected_intent_and_v2'] = (
                before_read['title'] in return_text and DRAFTS[1] in return_text and DRAFTS[0] not in return_text)
            checks['exactly_one_uncommitted_subject'] = (
                len([i for i in service.query({'open': True}) if i['kind'] == 'possibility']) == 1
                and all(i.get('commitment') != 'committed' for i in service.query()))
            checks['all_followups_routed_without_duplicate_work'] = all(
                service.get_item(i['id']).get('clarification', {}).get('target_item_id') == subject['id']
                and service.get_item(i['id'])['status'] == 'withdrawn' for i in captures[1:])
            materials = service.materials(subject['id'])
            checks['two_original_material_versions_retained'] = (
                [(m['id'], m['version'], m['valid']) for m in materials] ==
                [(material_id, 1, False), (material_id, 2, True)] and all(
                    service.read_material(subject['id'], material_id, index + 1)['content'] == content
                    for index, content in enumerate(DRAFTS)))
            checks['all_human_originals_retained'] = all(
                (root / i['original']['path']).read_text() == text
                and service.get_item(i['id'])['source_revisions'][0]['text'] == text
                for i, text in zip(captures, INPUTS))
            checks['original_saved_before_each_ack'] = saved_before_ack == [True] * 4
            checks['no_invented_recipients_dates_or_commitments'] = all(
                not i.get(key) for i in service.query()
                for key in ('recipient', 'recipients', 'due_at', 'review_at', 'starts_at', 'ends_at', 'decision_at'))
            checks['transport_only_owner_fake_http'] = (
                all(p['chat_id'] == 9 for p in http.sent)
                and all(name in {'getUpdates', 'sendMessage', 'answerCallbackQuery'} for name, _ in http.calls))
            phase('4_explicit_return_after_real_restart')
            return {'scenario': 'friends', 'checks': checks, 'phases': phases,
                    'scripted_decisions': decisions, 'pause_authority': paused_authority,
                    'paused_write_receipt': paused_write,
                    'simulation_limits': ['Deterministic screenplay; no Hermes inference.',
                        'Fake in-process Telegram HTTP; no external sends or accounts.',
                        'Real GTD service, SQLite, original files and material versions.',
                        'No inference about human relief or acceptance.'],
                    'final_subject': after_read,
                    'original_digests': [hashlib.sha256(t.encode()).hexdigest() for t in INPUTS]}
        finally:
            service.close()


class FriendsJourneyTests(unittest.IsolatedAsyncioTestCase):
    async def test_complete_friends_journey(self):
        result = await run_journey()
        self.assertEqual([], [name for name, passed in result['checks'].items() if not passed],
                         result['checks'])
