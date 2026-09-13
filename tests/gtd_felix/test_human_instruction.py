"""Human correction authority at the transactional domain boundary."""
from copy import deepcopy
from pathlib import Path
import sys
import tempfile
import unittest
from runtime_location import RUNTIME
sys.path.insert(0, str(RUNTIME))
from gtd_felix import GTDService


class HumanInstructionTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.s = GTDService(Path(self.tmp.name), owner_actor='human', principal_actor='principal', executor_actors=('executor',))
        self.n = 0
        self.target = self.s.capture('human', 'target', 'Asunto original')['item']
        self.target = self.command(self.target, 'clarify', {'kind': 'possibility', 'commitment': 'proposed'}, actor='human')['item']

    def tearDown(self):
        self.s.close()
        self.tmp.cleanup()

    def command(self, item, action, fields, actor='principal', operation_id=None):
        self.n += 1
        return self.s.execute(actor, dict(operation_id=operation_id or str(self.n), action=action,
            item_id=item['id'], expected_version=item['version'], fields=fields))

    def source(self, text='Corrige el asunto', source=None, actor='human'):
        self.n += 1
        return self.s.capture(actor, 'source-' + str(self.n), text, source=source or {})['item']

    def route(self, source, target=None):
        basis = {'source_item_id': source['id'], 'quote': source['source_revisions'][-1]['text']}
        result = self.command(source, 'clarify', dict(destination='existing', target_item_id=(target or self.target)['id'], reason='Instrucción humana', intent_basis=basis))
        self.assertEqual(result['status'], 'applied', result)
        return result['item']

    def fields(self, source, instruction='correct', changes=None):
        return dict(instruction=instruction, changes=({'title': 'Asunto corregido', 'text': 'Texto corregido'} if changes is None else changes),
            intent_basis=dict(source_item_id=source['id'], source_revision=len(source['source_revisions']), quote=source['source_revisions'][-1]['text']))

    def apply(self, source, **kwargs):
        return self.command(self.target, 'apply_human_instruction', self.fields(source, **kwargs))

    def test_correct_preserves_original_and_traces_real_actor_and_dependency(self):
        source = self.route(self.source())
        before = deepcopy(self.target)
        result = self.apply(source)
        self.assertEqual(result['status'], 'applied', result)
        item = result['item']
        self.assertEqual(item['title'], 'Asunto corregido')
        self.assertEqual(item['original'], before['original'])
        self.assertEqual(item['source_revisions'], before['source_revisions'])
        self.assertEqual(item['source_versions'][source['id']], 1)
        provenance = self.s.describe_item(item['id'])['field_provenance']['title']
        self.assertEqual(provenance['actor'], 'principal')
        self.assertEqual(provenance['human_authority']['intent_basis'], self.fields(source)['intent_basis'])
        self.assertEqual(source['clarification']['source_revision'], 1)

    def test_pause_keeps_material_current_and_correction_invalidates(self):
        material = self.command(self.target, 'put_material', {'content': 'Material útil'})
        self.target = material['item']
        source = self.route(self.source('Pausa este asunto'))
        result = self.apply(source, instruction='pause', changes={})
        self.assertEqual(result['status'], 'applied', result)
        self.assertEqual(result['item']['status'], 'paused')
        self.assertTrue(self.s.materials(self.target['id'])[0]['valid'])
        self.target = self.command(result['item'], 'reopen', {}, actor='human')['item']
        source = self.route(self.source())
        self.assertEqual(self.apply(source)['status'], 'applied')
        self.assertFalse(self.s.materials(self.target['id'])[0]['valid'])

    def test_principal_only_and_prohibited_fields(self):
        source = self.route(self.source())
        for actor in ('human', 'executor', 'stranger'):
            result = self.command(self.target, 'apply_human_instruction', self.fields(source), actor=actor)
            self.assertEqual(result['status'], 'rejected', result)
        for changes in ({}, {'status': 'done'}, {'commitment': 'committed'}, {'due_at': '2030-01-01'}, {'title': 'x', 'executor': 'executor'}):
            self.assertEqual(self.apply(source, changes=changes)['status'], 'rejected')
        self.assertEqual(self.apply(source, instruction='pause', changes={'title': 'x'})['status'], 'rejected')
        self.assertEqual(self.s.get_item(self.target['id']), self.target)

    def test_quote_revision_and_routing_fail_closed(self):
        source = self.source('No pauses este asunto')
        self.assertEqual(self.apply(source)['status'], 'rejected')
        source = self.route(source)
        for key, value in (('quote', 'pauses este asunto'), ('quote', 'Pausa'), ('source_revision', 0), ('source_revision', True), ('source_revision', 2)):
            fields = self.fields(source)
            fields['intent_basis'][key] = value
            self.assertEqual(self.command(self.target, 'apply_human_instruction', fields)['status'], 'rejected')
        other = self.source('Otro destino')
        self.assertEqual(self.command(other, 'apply_human_instruction', self.fields(source))['status'], 'rejected')
        self.target = self.command(self.target, 'edit', {'notes': 'Cambio posterior'}, actor='human')['item']
        self.assertEqual(self.apply(source)['error'], 'human_instruction_route_stale')

    def test_source_revision_after_route_and_new_revision_before_route(self):
        source = self.route(self.source())
        revised = self.s.revise_source('human', 'revise', source['id'], {}, text='No corrijas')['item']
        self.assertEqual(self.apply(source)['status'], 'rejected')
        self.assertEqual(self.apply(revised)['status'], 'rejected')
        source = self.source('Texto inicial')
        source = self.s.revise_source('human', 'revise2', source['id'], {}, text='Corrige el título')['item']
        source = self.route(source)
        self.assertEqual(self.apply(source)['status'], 'applied')

    def test_nested_forwarding_and_nonowner_sources(self):
        for metadata in ({'provider': 'gmail'}, {'provider': 'telegram', 'original_message': {'forward_origin': {'type': 'user'}}},
                         {'original_message': {'nested': [{'third_party': True}]}}, {'provider': 'local', 'forwarded': True}):
            source = self.source(source=metadata)
            result = self.command(source, 'clarify', dict(destination='existing', target_item_id=self.target['id'], reason='test',
                intent_basis={'source_item_id': source['id'], 'quote': source['text']}))
            self.assertEqual(result['status'], 'rejected', result)
        source = self.source(actor='principal')
        self.assertEqual(self.apply(source)['status'], 'rejected')

    def test_source_item_edit_after_route_cannot_reuse_old_authority(self):
        for changes in ({'title': 'No corregir'}, {'text': 'No corregir'}):
            source = self.route(self.source())
            edited = self.command(source, 'edit', changes, actor='human')
            self.assertEqual(edited['status'], 'applied', edited)
            self.assertEqual(self.apply(source)['error'], 'human_instruction_route_stale')
            self.assertEqual(self.s.get_item(self.target['id']), self.target)

    def test_agent_revision_cannot_become_human_authority(self):
        source = self.source()
        source = self.s.revise_source('principal', 'agent-revision', source['id'], {}, text='Pausa ahora')['item']
        result = self.command(source, 'clarify', dict(destination='existing', target_item_id=self.target['id'], reason='test',
            intent_basis={'source_item_id': source['id'], 'quote': 'Pausa ahora'}))
        self.assertEqual(result['error'], 'intent_basis_not_owner_direct')
        self.assertEqual(self.apply(source)['error'], 'intent_basis_not_owner_direct')

    def test_dependencies_originals_and_second_material_version_survive_pause_restart(self):
        source = self.route(self.source(source={'provider': 'local'}))
        self.target = self.apply(source)['item']
        first = self.command(self.target, 'put_material', {'content': 'Borrador uno'})['item']
        self.target = self.command(first, 'put_material', {'content': 'Borrador dos', 'material_id': first['materials'][0]['id']})['item']
        before_materials = self.s.materials(self.target['id'])
        before_dependencies = deepcopy(self.target['source_versions'])
        source2 = self.route(self.source('Pausa este asunto'))
        self.target = self.apply(source2, instruction='pause', changes={})['item']
        self.assertEqual(self.target['source_versions'], before_dependencies)
        self.assertEqual(self.s.materials(self.target['id']), before_materials)
        self.s.close()
        self.s = GTDService(Path(self.tmp.name), owner_actor='human', principal_actor='principal', executor_actors=('executor',))
        self.assertEqual(self.s.materials(self.target['id']), before_materials)
        self.assertTrue(self.s.materials(self.target['id'])[-1]['valid'])
        self.assertEqual(self.s.get_item(self.target['id']), self.target)
        for action, changes in (('edit', {'title': 'Otra'}), ('edit', {'text': 'Otro'}), ('edit', {'status': 'active'}), ('plan', {'title': 'Otra'})):
            self.assertEqual(self.command(self.target, action, changes)['status'], 'rejected')
        self.assertEqual(self.s.get_item(self.target['id']), self.target)

    def test_correct_merges_dependencies_and_target_semantics_are_bounded(self):
        first = self.route(self.source())
        self.target = self.apply(first)['item']
        second = self.route(self.source('Corrige de nuevo'))
        self.target = self.apply(second, changes={'text': 'Segunda versión'})['item']
        self.assertEqual(self.target['source_versions'], {first['id']: 1, second['id']: 1})
        for action, changes in (('edit', {'title': 'Otra'}), ('edit', {'text': 'Otro'}), ('edit', {'status': 'paused'}), ('plan', {'text': 'Otra'})):
            self.assertEqual(self.command(self.target, action, changes)['status'], 'rejected')
        source = self.route(self.source())
        fields = self.fields(source)
        fields['extra'] = True
        self.assertEqual(self.command(self.target, 'apply_human_instruction', fields)['error'], 'invalid_human_instruction')
        stale = dict(self.target, version=self.target['version'] - 1)
        self.assertEqual(self.command(stale, 'apply_human_instruction', self.fields(source))['status'], 'conflict')
        # Failed validation did not consume the direct source.
        self.assertEqual(self.apply(source)['status'], 'applied')
        self.target = self.s.get_item(self.target['id'])
        self.target = self.command(self.target, 'clarify', {'kind': 'action', 'commitment': 'committed'}, actor='human')['item']
        source = self.route(self.source())
        self.assertEqual(self.apply(source)['error'], 'human_instruction_target_invalid')
        self.assertEqual(self.apply(source, instruction='pause', changes={})['status'], 'applied')

    def test_consumption_replay_and_operation_conflict(self):
        source = self.route(self.source())
        fields = self.fields(source)
        result = self.command(self.target, 'apply_human_instruction', fields, operation_id='apply')
        self.assertEqual(result['status'], 'applied', result)
        self.assertEqual(self.command(self.target, 'apply_human_instruction', fields, operation_id='apply')['status'], 'already_applied')
        changed = deepcopy(fields)
        changed['changes']['title'] = 'Otra corrección'
        self.assertEqual(self.command(self.target, 'apply_human_instruction', changed, operation_id='apply')['error'], 'operation_id_reused')
        self.target = result['item']
        self.assertEqual(self.command(self.target, 'apply_human_instruction', fields)['error'], 'human_instruction_source_consumed')
        self.assertEqual(self.s.get_item(self.target['id']), self.target)


if __name__ == '__main__':
    unittest.main()
