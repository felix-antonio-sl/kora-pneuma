"""Routed direct owner intent through a real admitted HTTP principal job."""
import unittest
from datetime import datetime, timezone
import test_application as fixtures


class RoutedIntentTests(unittest.IsolatedAsyncioTestCase):
    asyncSetUp = fixtures.HTTPTests.asyncSetUp
    asyncTearDown = fixtures.HTTPTests.asyncTearDown
    agent_command = fixtures.HTTPTests.agent_command

    def setup_route(self, *, admitted=True, routed=True, metadata=None, actor='felix', target_fields=None):
        self.control.config = dict(period_start=datetime.now(timezone.utc).isoformat(), period_seconds=3600,
            max_cost_usd=10, max_runtime_seconds=1000, recovery_cost_usd=1, recovery_runtime_seconds=50,
            max_active=2, max_job_runtime_seconds=300, max_retries=0, max_descendants=1)
        target = self.service.capture('felix', 'target', 'Please update my fronts')['item']
        if target_fields:
            target = self.service.execute('felix', {'operation_id': 'prior-target-fields', 'action': 'edit',
                'item_id': target['id'], 'expected_version': target['version'], 'fields': target_fields})['item']
        source = self.service.capture(actor, 'reply', 'Prepare a private map of responsibilities and next steps.',
            source=metadata or {'provider': 'telegram'})['item']
        if routed:
            result = self.service.execute('gtd-felix', {'operation_id': 'route', 'action': 'clarify',
                'item_id': source['id'], 'expected_version': source['version'],
                'fields': {'destination': 'existing', 'target_item_id': target['id'], 'reason': 'Direct reply',
                    'intent_basis': {'source_item_id': source['id'], 'quote': source['text']}}})
            self.assertEqual('applied', result['status'], result)
            source = result['item']
        self.control.register_bot('felix', 'register', {'id': 'principal', 'state': 'available',
            'source_urn': 'urn:test:principal', 'host': 'synthetic', 'profile': 'fixture',
            'capabilities': ['prepare_private'], 'probe_evidence': 'fixture://probe'})
        result = self.control.reserve('gtd-felix', 'reserve', {'item_id': target['id'], 'expected_version': target['version'],
            'capability': 'prepare_private', 'bot_id': 'principal', 'mandate_id': None, 'purpose': 'Private map',
            'scope': 'Private only', 'max_cost_usd': 2, 'max_runtime_seconds': 60, 'max_retries': 0,
            'max_descendants': 0, 'human_instruction_source_ids': [source['id']] if admitted else []})
        self.assertEqual('reserved', result['status'], result)
        fields = {'kind': 'project', 'commitment': 'committed', 'capability': 'prepare_private',
            'completion_criteria': 'Private map of current responsibilities and next steps',
            'intent_basis': {'source_item_id': source['id'], 'quote': source['text']}}
        return target, source, result['job_id'], fields

    async def test_routed_current_direct_full_quote_prepares_target_and_preserves_provenance(self):
        target, source, job, fields = self.setup_route()
        result = await self.agent_command(job, target, 'prepare', 'clarify', fields)
        self.assertEqual('applied', result['status'], result)
        item = result['item']
        self.assertEqual('gtd-felix', item['executor'])
        self.assertEqual('prepare_private', item['work_capability'])
        self.assertEqual(source['id'], item['intent_basis']['source_item_id'])
        self.assertEqual('gtd-felix', item['intent_basis']['interpreted_by'])
        self.assertEqual(target['source_revisions'], item['source_revisions'])
        self.assertEqual(source, self.service.get_item(source['id']))
        self.assertFalse(item.get('mandate_id'))
        plan = await self.agent_command(job, item, 'plan', 'plan', {'plan_steps': ['Prepare the private map']})
        self.assertEqual('applied', plan['status'], plan)

    async def test_later_routed_reply_invalidates_old_job_until_all_sources_admitted(self):
        target, source, job, fields = self.setup_route()
        later = self.service.capture('felix', 'later-reply', 'Stop and review the scope before preparing.',
            source={'provider': 'telegram'})['item']
        routed = self.service.execute('gtd-felix', {'operation_id': 'later-route', 'action': 'clarify',
            'item_id': later['id'], 'expected_version': later['version'], 'fields': {
                'destination': 'existing', 'target_item_id': target['id'], 'reason': 'Later human response',
                'intent_basis': {'source_item_id': later['id'], 'quote': later['text']}}})
        self.assertEqual('applied', routed['status'], routed)
        result = await self.agent_command(job, target, 'old-prepare', 'clarify', fields)
        self.assertEqual('routed_intent_set_stale', result['error'])
        plan = await self.agent_command(job, target, 'old-plan', 'plan', {'plan_steps': ['Continue old scope']})
        self.assertEqual('routed_intent_set_stale', plan['error'])
        self.assertEqual(target, self.service.get_item(target['id']))
        fixtures.HTTPTests.finish_scope_job(self, job)
        old = self.control.get_job(job)
        request = {key: old[key] for key in ('capability', 'bot_id', 'mandate_id', 'purpose', 'scope',
            'max_cost_usd', 'max_runtime_seconds', 'max_retries', 'max_descendants')}
        reserved = self.control.reserve('gtd-felix', 'complete-admission', {**request,
            'item_id': target['id'], 'expected_version': target['version'],
            'human_instruction_source_ids': [source['id'], later['id']]})
        self.assertEqual('reserved', reserved['status'], reserved)
        # Having both replies permits reconsideration, not an inferred mandate
        # to execute the old request. The new principal may record only a plan.
        plan = await self.agent_command(reserved['job_id'], target, 'new-plan', 'plan',
            {'plan_steps': ['Reconcile both human responses before any preparation']})
        self.assertEqual('applied', plan['status'], plan)

    async def test_later_routed_reply_also_invalidates_job_after_project_clarification(self):
        target, source, job, fields = self.setup_route()
        prepared = await self.agent_command(job, target, 'prepare-project', 'clarify', fields)
        self.assertEqual('applied', prepared['status'], prepared)
        project = prepared['item']
        later = self.service.capture('felix', 'project-stop', 'Stop; reconsider the prepared project.',
            source={'provider': 'telegram'})['item']
        routed = self.service.execute('gtd-felix', {'operation_id': 'project-route', 'action': 'clarify',
            'item_id': later['id'], 'expected_version': later['version'], 'fields': {
                'destination': 'existing', 'target_item_id': project['id'], 'reason': 'Later direction',
                'intent_basis': {'source_item_id': later['id'], 'quote': later['text']}}})
        self.assertEqual('applied', routed['status'], routed)
        for operation, action, command_fields in [('old-plan', 'plan', {'plan_steps': ['Continue']}),
                ('old-material', 'put_material', {'content': 'Old preparation'})]:
            result = await self.agent_command(job, project, operation, action, command_fields)
            self.assertEqual('routed_intent_set_stale', result['error'], result)
        self.assertEqual(project, self.service.get_item(project['id']))

    async def test_source_not_admitted_to_job_rejected(self):
        target, source, job, fields = self.setup_route(admitted=False)
        result = await self.agent_command(job, target, 'prepare', 'clarify', fields)
        self.assertEqual('routed_intent_set_stale', result['error'])
        self.assertEqual(target, self.service.get_item(target['id']))

    async def test_unrouted_source_rejected(self):
        target, source, job, fields = self.setup_route(routed=False)
        result = await self.agent_command(job, target, 'prepare', 'clarify', fields)
        self.assertEqual('human_instruction_source_not_routed', result['error'])

    async def test_partial_quote_rejected(self):
        target, source, job, fields = self.setup_route()
        fields['intent_basis']['quote'] = 'Prepare a private map'
        result = await self.agent_command(job, target, 'prepare', 'clarify', fields)
        self.assertEqual('intent_basis_not_owner_direct', result['error'])

    async def test_revised_source_invalidates_job_and_domain_route(self):
        target, source, job, fields = self.setup_route()
        self.service.revise_source('felix', 'new-reply', source['id'], {'provider': 'telegram'}, text='Changed request')
        result = await self.agent_command(job, target, 'prepare', 'clarify', fields)
        self.assertEqual('rejected', result['status'])
        direct = self.service.execute('gtd-felix', {'operation_id': 'direct', 'action': 'clarify',
            'item_id': target['id'], 'expected_version': target['version'], 'fields': fields})
        self.assertIn(direct['error'], {'source_version_stale', 'human_instruction_route_stale'})

    async def test_routed_intent_does_not_grant_dates(self):
        target, source, job, fields = self.setup_route()
        fields['due_at'] = '2026-10-01'
        result = await self.agent_command(job, target, 'prepare', 'clarify', fields)
        self.assertEqual('routed_private_intent_fields_restricted', result['error'])

    async def test_forwarded_or_foreign_source_cannot_be_routed(self):
        for index, metadata in enumerate(({'provider': 'gmail'}, {'provider': 'telegram', 'forward_origin': {'type': 'user'}})):
            target = self.service.capture('felix', f'target-{index}', 'Target')['item']
            source = self.service.capture('felix', f'foreign-{index}', 'Prepare something', source=metadata)['item']
            result = self.service.execute('gtd-felix', {'operation_id': f'route-{index}', 'action': 'clarify',
                'item_id': source['id'], 'expected_version': source['version'], 'fields': {
                    'destination': 'existing', 'target_item_id': target['id'], 'reason': 'Invalid source',
                    'intent_basis': {'source_item_id': source['id'], 'quote': source['text']}}})
            self.assertEqual('intent_basis_not_owner_direct', result['error'])

    async def test_route_to_other_target_is_not_authority(self):
        target, source, job, fields = self.setup_route()
        other = self.service.capture('felix', 'other', 'Other target')['item']
        result = self.service.execute('gtd-felix', {'operation_id': 'other-prepare', 'action': 'clarify',
            'item_id': other['id'], 'expected_version': other['version'], 'fields': fields})
        self.assertEqual('human_instruction_source_not_routed', result['error'])

    def fresh_job(self, target, previous):
        fixtures.HTTPTests.finish_scope_job(self, previous)
        job = self.control.get_job(previous)
        request = {key: job[key] for key in ('capability', 'bot_id', 'mandate_id', 'purpose', 'scope',
            'max_cost_usd', 'max_runtime_seconds', 'max_retries', 'max_descendants', 'human_instruction_source_ids')}
        result = self.control.reserve('gtd-felix', 'fresh-reserve', {**request,
            'item_id': target['id'], 'expected_version': target['version']})
        self.assertEqual('reserved', result['status'], result)
        return result['job_id']

    async def test_principal_plan_advance_requires_fresh_job_but_keeps_route_valid(self):
        target, source, job, fields = self.setup_route()
        planned = self.service.execute('gtd-felix', {'operation_id': 'technical-plan', 'action': 'plan',
            'item_id': target['id'], 'expected_version': target['version'],
            'fields': {'plan_steps': ['Inspect current map'], 'uncertainties': ['Missing current status']}})
        self.assertEqual('applied', planned['status'], planned)
        result = await self.agent_command(job, planned['item'], 'old-job', 'clarify', fields)
        self.assertEqual('rejected', result['status'])
        fresh = self.fresh_job(planned['item'], job)
        result = await self.agent_command(fresh, planned['item'], 'fresh-prepare', 'clarify', fields)
        self.assertEqual('applied', result['status'], result)
        self.assertEqual(source['clarification'], self.service.get_item(source['id'])['clarification'])

    async def test_owner_plan_change_is_not_compatible_preparation(self):
        target, source, job, fields = self.setup_route()
        changed = self.service.execute('felix', {'operation_id': 'human-plan', 'action': 'edit',
            'item_id': target['id'], 'expected_version': target['version'], 'fields': {'plan_steps': ['Human correction']}})['item']
        fresh = self.fresh_job(changed, job)
        result = await self.agent_command(fresh, changed, 'prepare', 'clarify', fields)
        self.assertEqual('human_instruction_route_stale', result['error'])

    async def test_material_target_changes_reject_route_in_domain(self):
        target, source, job, fields = self.setup_route()
        for index, change in enumerate(({'due_at': '2026-10-01'}, {'source': {'provider': 'telegram', 'revision': 'new'}},
                                        {'status': 'paused'})):
            current = self.service.get_item(target['id'])
            changed = self.service.execute('felix', {'operation_id': f'change-{index}', 'action': 'pause' if 'status' in change else 'edit',
                'item_id': current['id'], 'expected_version': current['version'], 'fields': {} if 'status' in change else change})
            self.assertEqual('applied', changed['status'], changed)
            result = self.service.execute('gtd-felix', {'operation_id': f'prepare-{index}', 'action': 'clarify',
                'item_id': current['id'], 'expected_version': changed['item']['version'], 'fields': fields})
            self.assertEqual('rejected', result['status'], result)


    def pause_and_reopen(self, target):
        paused = self.service.execute('felix', {'operation_id': 'explicit-pause', 'action': 'pause',
            'item_id': target['id'], 'expected_version': target['version']})
        self.assertEqual('applied', paused['status'], paused)
        reopened = self.service.execute('felix', {'operation_id': 'explicit-reopen', 'action': 'reopen',
            'item_id': target['id'], 'expected_version': paused['item']['version']})
        self.assertEqual('applied', reopened['status'], reopened)
        return reopened['item']

    async def test_attested_owner_pause_reopen_allows_fresh_routed_job(self):
        target, source, job, fields = self.setup_route()
        current = self.pause_and_reopen(target)
        fresh = self.fresh_job(current, job)
        result = await self.agent_command(fresh, current, 'resume-prepare', 'clarify', fields)
        self.assertEqual('applied', result['status'], result)
        self.assertEqual(source['clarification'], self.service.get_item(source['id'])['clarification'])
        self.assertEqual({'action': 'pause', 'item_id': target['id'], 'applied_version': 2},
            self.service._meta('owner_state_action:explicit-pause'))

    async def test_attested_pause_reopen_before_route_allows_fresh_job(self):
        target, source, job, fields = self.setup_route(routed=False)
        current = self.pause_and_reopen(target)
        route = self.service.execute('gtd-felix', {'operation_id': 'route-after-return', 'action': 'clarify',
            'item_id': source['id'], 'expected_version': source['version'], 'fields': {
                'destination': 'existing', 'target_item_id': current['id'], 'reason': 'Direct reply after return',
                'intent_basis': fields['intent_basis']}})
        self.assertEqual('applied', route['status'], route)
        fresh = self.fresh_job(current, job)
        result = await self.agent_command(fresh, current, 'prepare-after-route', 'clarify', fields)
        self.assertEqual('applied', result['status'], result)

    async def test_pause_reopen_before_route_does_not_hide_erased_human_return(self):
        target, source, job, fields = self.setup_route(routed=False, target_fields={'review_at': '2026-10-01'})
        current = self.pause_and_reopen(target)
        route = self.service.execute('gtd-felix', {'operation_id': 'route-after-dated-return', 'action': 'clarify',
            'item_id': source['id'], 'expected_version': source['version'], 'fields': {
                'destination': 'existing', 'target_item_id': current['id'], 'reason': 'Direct reply after return',
                'intent_basis': fields['intent_basis']}})
        self.assertEqual('applied', route['status'], route)
        fresh = self.fresh_job(current, job)
        result = await self.agent_command(fresh, current, 'prepare-after-dated-route', 'clarify', fields)
        self.assertEqual('human_position_protected', result['error'])

    async def test_legacy_unattested_pause_reopen_fails_closed(self):
        target, source, job, fields = self.setup_route()
        current = self.pause_and_reopen(target)
        self.service.store.db.execute("DELETE FROM metadata WHERE key='owner_state_action:explicit-pause'")
        result = self.service.execute('gtd-felix', {'operation_id': 'legacy-prepare', 'action': 'clarify',
            'item_id': current['id'], 'expected_version': current['version'], 'fields': fields})
        self.assertEqual('human_instruction_route_stale', result['error'])

    async def test_reopen_clearing_prior_human_return_is_not_compatible(self):
        target, source, job, fields = self.setup_route(target_fields={'review_at': '2026-10-01'})
        current = self.pause_and_reopen(target)
        result = self.service.execute('gtd-felix', {'operation_id': 'dated-prepare', 'action': 'clarify',
            'item_id': current['id'], 'expected_version': current['version'], 'fields': fields})
        self.assertEqual('human_instruction_route_stale', result['error'])



import test_orchestration as orchestration_fixtures
from gtd_felix.orchestration import OrchestrationWorker


class RoutedIntentRecoveryTests(unittest.IsolatedAsyncioTestCase):
    asyncSetUp = orchestration_fixtures.OrchestrationTests.asyncSetUp
    asyncTearDown = orchestration_fixtures.OrchestrationTests.asyncTearDown

    async def test_owner_reopen_continuation_admits_current_routed_sources(self):
        source = self.previous_route()
        orchestration_fixtures.OrchestrationTests.make_private_action(self)
        item = self.service.get_item(self.item['id'])
        review = self.service.execute('felix', {'operation_id': 'initial-private-review',
            'action': 'request_review', 'item_id': item['id'],
            'expected_version': item['version'], 'fields': {}})
        self.assertEqual('applied', review['status'], review)
        self.native.complete_criterion = True
        await self.worker.tick()
        await self.worker.tick()
        item = self.service.get_item(item['id'])
        self.assertEqual('done', item['status'])
        origin = self.control.get_job(self.native.submissions[-1]['job_id'])
        self.assertIn(source['id'], origin['human_instruction_source_ids'])
        reopened = self.service.execute('felix', {'operation_id': 'owner-reopen-private',
            'action': 'reopen', 'item_id': item['id'], 'expected_version': item['version']})
        self.assertEqual('applied', reopened['status'], reopened)
        self.native.no_progress = True
        self.worker = OrchestrationWorker(self.service, self.control, self.native, self.config)
        await self.worker.tick()
        job = self.control.get_job(self.native.submissions[-1]['job_id'])
        self.assertNotEqual(origin['id'], job['id'])
        self.assertIn(source['id'], job.get('human_instruction_source_ids', []))
        self.assertEqual(self.control._basis(source['id']), job['source_bases'][source['id']])
        self.assertTrue(self.control.validate_target(job['id'], 'gtd-felix', item['id'],
            'prepare_private')['allowed'])
        self.assertIn(source['text'], self.native.submissions[-1]['prompt'])
        self.assertEqual(2, len(self.native.submissions))
        planned = await self.client.call('gtd_command', {'job_id': job['id'], 'command': {
            'operation_id': 'reopened-job-plan', 'action': 'plan', 'item_id': item['id'],
            'expected_version': reopened['item']['version'],
            'fields': {'plan_steps': ['Review the original human direction before preparing']}}})
        self.assertEqual('applied', planned['status'], planned)
        later = self.service.capture('felix', 'later-reopened-reply', 'Wait for my corrected scope.',
            source={'provider': 'telegram'})['item']
        routed = self.service.execute('gtd-felix', {'operation_id': 'route-after-reopened-admission',
            'action': 'clarify', 'item_id': later['id'], 'expected_version': later['version'],
            'fields': {'destination': 'existing', 'target_item_id': item['id'], 'reason': 'Later reply',
                'intent_basis': {'source_item_id': later['id'], 'quote': later['text']}}})
        self.assertEqual('applied', routed['status'], routed)
        self.assertEqual('routed_intent_set_stale', self.control.validate_target(
            job['id'], 'gtd-felix', item['id'], 'prepare_private')['reason'])

    def previous_route(self):
        source = self.service.capture('felix', 'routed-reply', 'Prepare a private map of current work.',
            source={'provider': 'telegram'})['item']
        routed = self.service.execute('gtd-felix', {'operation_id': 'route-reply', 'action': 'clarify',
            'item_id': source['id'], 'expected_version': source['version'], 'fields': {
                'destination': 'existing', 'target_item_id': self.item['id'], 'reason': 'Direct clarification',
                'intent_basis': {'source_item_id': source['id'], 'quote': source['text']}}})
        self.assertEqual('applied', routed['status'], routed)
        for event in self.service.pending_events('gtd-review', 'local'):
            self.service.mark_event(event['event_key'], 'done')
        self.service.mark_event(self.event['event_key'], 'done')
        return routed['item']

    async def test_new_review_recovers_pending_intent_without_reopening_consumed_event(self):
        source = self.previous_route()
        planned = self.service.execute('gtd-felix', {'operation_id': 'only-plan', 'action': 'plan',
            'item_id': self.item['id'], 'expected_version': self.item['version'],
            'fields': {'plan_steps': ['Prepare map']}})
        self.assertEqual('applied', planned['status'], planned)
        for event in self.service.pending_events('gtd-review', 'local'):
            self.service.mark_event(event['event_key'], 'done')
        self.service.ingest_event({'provider': 'gtd-review', 'account': 'local', 'external_id': 'fresh-gap',
            'revision': '1', 'payload': {'item_id': self.item['id'], 'reason': 'periodic_gap'}})
        self.native.no_progress = True
        self.worker = OrchestrationWorker(self.service, self.control, self.native, self.config)
        await self.worker.tick()
        submission = self.native.submissions[-1]
        job = self.control.get_job(submission['job_id'])
        self.assertIn(source['id'], job['human_instruction_source_ids'])
        self.assertIn('pending_routed_intents', submission['prompt'])
        self.assertIn(source['text'], submission['prompt'])
        self.assertEqual('done', self.service.store.db.execute(
            "SELECT status FROM events WHERE external_id=?", ('routed:' + source['id'],)).fetchone()[0])

    async def test_consumed_stale_or_clarified_intent_is_not_recovered(self):
        from gtd_felix.domain import fingerprint
        source = self.previous_route()
        self.assertEqual(1, len(self.worker._pending_routed_intents(self.item)))
        key = 'human_instruction:' + fingerprint([source['id'], 1])
        self.service._set_meta(key, {'operation_id': 'synthetic-consumed'})
        self.assertEqual([], self.worker._pending_routed_intents(self.item))
        self.service.store.db.execute('DELETE FROM metadata WHERE key=?', (key,))
        self.service.revise_source('felix', 'revised', source['id'], {'provider': 'telegram'}, text='New instruction')
        self.assertEqual([], self.worker._pending_routed_intents(self.item))
        self.assertEqual([], self.worker._pending_routed_intents({**self.item, 'kind': 'project'}))

    async def test_recent_conversation_context_is_bounded_direct_and_same_chat(self):
        stamp = 1789300000
        def capture(identity, text, date, **extra):
            return self.service.capture('felix', identity, text, source={
                'provider': 'telegram', 'account': 'bot', 'chat_id': 9,
                'message_id': date, 'date': date, **extra})['item']
        old = capture('old', 'Outside the time window', stamp - 90000)
        other = capture('other-chat', 'Unrelated private chat', stamp - 10, chat_id=10)
        forwarded = capture('forwarded', 'Forwarded third-party order', stamp - 9,
            forward_origin={'type': 'user'})
        for index in range(15):
            capture(f'prior-{index}', f'Previous direct turn {index}', stamp - 100 + index)
        previous = capture('deadline-context', 'Todo esto antes del lunes.', stamp - 3)
        previous = self.service.execute('gtd-felix', {'operation_id': 'date-question', 'action': 'plan',
            'item_id': previous['id'], 'expected_version': previous['version'],
            'fields': {'decision_needed': True, 'decision_question': '¿Qué fecha corresponde a ese lunes?'}})['item']
        answer = capture('date-answer', 'El lunes 14; el mapa es para mi asistencia.', stamp)
        self.worker = OrchestrationWorker(self.service, self.control, self.native, self.config)
        context = self.worker._recent_human_context(answer, {})
        self.assertEqual(12, len(context))
        self.assertEqual(sorted(entry['date'] for entry in context), [entry['date'] for entry in context])
        self.assertIn(previous['id'], {entry['id'] for entry in context})
        self.assertFalse({old['id'], other['id'], forwarded['id'], answer['id']} & {entry['id'] for entry in context})
        entry = next(entry for entry in context if entry['id'] == previous['id'])
        self.assertEqual('Todo esto antes del lunes.', entry['text'])
        self.assertEqual('¿Qué fecha corresponde a ese lunes?', entry['decision_question'])
        self.assertEqual(stamp - 3, entry['date'])
        self.assertEqual(previous['version'], entry['version'])
        self.assertEqual([], self.worker._recent_human_context({**answer, 'source': {'provider': 'gmail'}}, {}))

    async def test_explicit_review_is_one_new_admission_without_changed_meaning(self):
        self.native.no_progress = True
        await self.worker.tick()
        await self.worker.tick()
        item = self.service.get_item(self.item['id'])
        before = len(self.native.submissions)
        command = {'operation_id': 'retry-review-once', 'action': 'request_review',
            'item_id': item['id'], 'expected_version': item['version'], 'fields': {}}
        receipt = self.service.execute('felix', command)
        self.assertEqual('applied', receipt['status'], receipt)
        self.assertEqual(item, self.service.get_item(item['id']))
        self.worker = OrchestrationWorker(self.service, self.control, self.native, self.config)
        await self.worker.tick()
        self.assertEqual(before + 1, len(self.native.submissions))
        self.assertEqual('already_applied', self.service.execute('felix', command)['status'])
        await self.worker.tick()
        await self.worker.tick()
        self.assertEqual(before + 1, len(self.native.submissions))

    async def test_explicit_review_after_principal_write_is_not_own_event(self):
        self.native.clarify_only = True
        await self.worker.tick()
        await self.worker.tick()
        item = self.service.get_item(self.item['id'])
        self.assertGreater(item['version'], 1)
        before = len(self.native.submissions)
        receipt = self.service.execute('felix', {
            'operation_id': 'review-after-principal', 'action': 'request_review',
            'item_id': item['id'], 'expected_version': item['version'], 'fields': {}})
        self.assertEqual('applied', receipt['status'])
        await self.worker.tick()
        self.assertEqual(before + 1, len(self.native.submissions))
        await self.worker.tick()
        await self.worker.tick()
        self.assertEqual(before + 1, len(self.native.submissions))

    async def test_unaccredited_review_event_is_ignored(self):
        for version in [1, '1', None, True]:
            event = {'provider': 'gtd-review', 'account': 'local', 'event_key': 'forged',
                'payload': {'reason': 'requested_review', 'item_id': self.item['id'],
                    'version': version, 'operation_id': 'missing'}}
            self.assertTrue(self.worker._own_event(event))
        for operation_id in [{}, [], None]:
            event['payload'].update(version=1, operation_id=operation_id)
            self.assertTrue(self.worker._own_event(event))

    async def test_native_reply_keeps_complete_text_without_payload_duplication(self):
        self.native.no_progress = True
        await self.worker.tick()
        job_id = self.native.submissions[-1]['job_id']
        self.native.runs[job_id]['output'] = 'R' * 7000
        await self.worker.tick()
        events = self.service.pending_events('gtd-notification', 'local')
        payload = next(event['payload'] for event in events if event['external_id'] == job_id)
        self.assertEqual('R' * 7000, payload['native_reply'])
        self.assertNotIn('R' * 100, payload['text'])


class RequestedReviewTests(unittest.IsolatedAsyncioTestCase):
    asyncSetUp = fixtures.HTTPTests.asyncSetUp
    asyncTearDown = fixtures.HTTPTests.asyncTearDown
    request = fixtures.HTTPTests.request

    async def test_owner_http_request_is_durable_idempotent_and_preserves_item(self):
        from gtd_felix.service import GTDService
        item = self.service.capture('felix', 'review-target', 'Target')['item']
        command = {'operation_id': 'explicit-review', 'action': 'request_review',
            'item_id': item['id'], 'expected_version': item['version'], 'fields': {}}
        status, first = await self.request('POST', '/v1/commands', json=command)
        self.assertEqual(200, status)
        self.assertEqual('applied', first['status'], first)
        self.assertEqual(item, self.service.get_item(item['id']))
        await self.runner.cleanup()
        self.service.close()
        self.service = GTDService(__import__('pathlib').Path(self.config['data_dir']), executor_actors=['worker'])
        replay = self.service.execute('felix', command)
        self.assertEqual('already_applied', replay['status'])
        self.assertEqual(first['event_key'], replay['event_key'])
        self.assertEqual(1, self.service.store.db.execute('SELECT count(*) FROM events WHERE event_key=?',
            (first['event_key'],)).fetchone()[0])

    async def test_actor_version_and_pause_guards(self):
        item = self.service.capture('felix', 'review-target', 'Target')['item']
        command = {'operation_id': 'not-owner', 'action': 'request_review',
            'item_id': item['id'], 'expected_version': item['version'], 'fields': {}}
        rejected = self.service.execute('gtd-felix', command)
        self.assertEqual('owner_required', rejected['error'])
        changed = self.service.execute('felix', {'operation_id': 'pause', 'action': 'pause',
            'item_id': item['id'], 'expected_version': item['version']})['item']
        stale = self.service.execute('felix', {**command, 'operation_id': 'stale'})
        self.assertEqual('conflict', stale['status'])
        paused = self.service.execute('felix', {**command, 'operation_id': 'paused', 'expected_version': changed['version']})
        self.assertEqual('work_paused', paused['error'])
        self.assertEqual(changed, self.service.get_item(item['id']))
        self.assertFalse(any(event['payload'].get('reason') == 'requested_review'
            for event in self.service.pending_events('gtd-review', 'local')))
