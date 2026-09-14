"""A new admitted parent revises only its principal-owned child dependency."""
import unittest
import test_application as http


class RefreshTests(unittest.IsolatedAsyncioTestCase):
    asyncSetUp = http.HTTPTests.asyncSetUp
    asyncTearDown = http.HTTPTests.asyncTearDown
    private_job = http.HTTPTests.private_job
    agent_command = http.HTTPTests.agent_command
    finish_scope_job = http.HTTPTests.finish_scope_job
    reserve_private_scope = http.HTTPTests.reserve_private_scope

    async def scenario(self):
        source, old = self.private_job('Meeting 10:00; maximum 12 people, room pending')
        derived = await self.agent_command(old, source, 'derive-preparation', 'derive', {
            'kind': 'action', 'title': 'Prepare meeting', 'capability': 'prepare_private',
            'completion_criteria': 'Private meeting package', 'source_versions': {source['id']: 1}})
        self.assertEqual(derived['status'], 'applied', derived)
        child = derived['item']
        material = await self.agent_command(old, child, 'material-r1', 'put_material', {
            'content': 'Meeting 10:00; maximum 12 people, room pending', 'source_versions': {source['id']: 1}})
        self.assertEqual(material['status'], 'applied', material)
        child = material['item']
        self.finish_scope_job(old)
        revised = self.service.revise_source('felix', 'source-r2', source['id'], source={'revision': '2'}, text='Meeting 09:30; maximum 12 people, room pending')
        self.assertEqual(revised['status'], 'applied', revised)
        return revised['item'], child, old

    async def test_same_child_new_parent_job_refresh_material_and_new_child_admission(self):
        source, child, old = await self.scenario()
        previous = self.control.get_job(old)
        request = {key: previous[key] for key in ('capability', 'bot_id', 'purpose', 'scope', 'max_cost_usd', 'max_runtime_seconds', 'max_retries', 'max_descendants', 'mandate_id')}
        rejected = self.control.reserve('gtd-felix', 'direct-stale', {**request, 'item_id': child['id'], 'expected_version': child['version']})
        self.assertEqual(rejected['error'], 'source_version_stale')
        job = self.reserve_private_scope(source, old, 'new-parent')
        changed = await self.agent_command(job, child, 'refresh-r2', 'plan', {'source_versions': {source['id']: 2}})
        self.assertEqual(changed['status'], 'applied', changed)
        self.assertEqual(changed['item']['id'], child['id'])
        for key in ('title', 'completion_criteria', 'commitment', 'executor', 'status'):
            self.assertEqual(changed['item'].get(key), child.get(key))
        replay = await self.agent_command(job, child, 'refresh-r2', 'plan', {'source_versions': {source['id']: 2}})
        self.assertEqual(replay['status'], 'already_applied', replay)
        old_attempt = await self.agent_command(old, changed['item'], 'old-refresh', 'plan', {'source_versions': {source['id']: 2}})
        self.assertEqual(old_attempt['status'], 'rejected')
        materials = self.service.materials(child['id'])
        self.assertFalse(materials[0]['valid'])
        # I2: documents carry references; identity resolves by digest.
        self.assertEqual(materials[0]['original']['sha256'], child['materials'][0]['digest'])
        fresh = await self.agent_command(job, changed['item'], 'material-r2', 'put_material', {
            'content': 'Meeting 09:30; maximum 12 people, room pending', 'material_id': materials[0]['id'], 'source_versions': {source['id']: 2}})
        self.assertEqual(fresh['status'], 'applied', fresh)
        self.finish_scope_job(job)
        new_child_job = self.reserve_private_scope(fresh['item'], job, 'new-child')
        self.assertTrue(self.control.validate(new_child_job, 'prepare_private')['allowed'])
        self.assertEqual(len(self.service.query()), 2)

    async def test_owner_mapping_even_identical_echo_is_protected(self):
        source, child, old = await self.scenario()
        owned = self.service.execute('felix', {'operation_id': 'owner-sources', 'action': 'plan', 'item_id': child['id'],
            'expected_version': child['version'], 'fields': {'source_versions': {source['id']: 2}}})['item']
        job = self.reserve_private_scope(source, old, 'new-parent')
        result = await self.agent_command(job, owned, 'echo-owner', 'plan', {'source_versions': {source['id']: 2}})
        self.assertEqual(result.get('error'), 'human_position_protected')
        self.assertEqual(self.service.get_item(child['id']), owned)

    async def test_keyset_and_noncurrent_revisions_rejected_atomically(self):
        source, child, old = await self.scenario()
        job = self.reserve_private_scope(source, old, 'new-parent')
        for i, mapping in enumerate(({}, {'absent': 2}, {source['id']: 1}, {source['id']: 3})):
            result = await self.agent_command(job, child, 'bad-' + str(i), 'plan', {'source_versions': mapping, 'plan_steps': ['must not apply']})
            self.assertEqual(result['status'], 'rejected', result)
            self.assertEqual(self.service.get_item(child['id']), child)

    async def test_new_external_revision_after_admission_rejects_refresh(self):
        source, child, old = await self.scenario()
        job = self.reserve_private_scope(source, old, 'new-parent')
        self.service.revise_source('felix', 'source-r3', source['id'], source={'revision': '3'}, text='Meeting 09:00')
        result = await self.agent_command(job, child, 'refresh-r3', 'plan', {'source_versions': {source['id']: 3}})
        self.assertEqual(result['status'], 'rejected', result)
        self.assertEqual(self.service.get_item(child['id']), child)

    async def test_uncaptured_external_source_cannot_be_added_to_job_snapshot(self):
        parent, old = self.private_job()
        source = self.service.capture('felix', 'outside-source', 'External r1')['item']
        child = self.service.execute('gtd-felix', {'operation_id': 'external-derived', 'action': 'derive',
            'item_id': parent['id'], 'expected_version': parent['version'], 'fields': {
                'kind': 'action', 'title': 'Existing external dependency', 'capability': 'prepare_private',
                'source_versions': {source['id']: 1}}})['item']
        self.finish_scope_job(old)
        self.service.revise_source('felix', 'external-r2', source['id'], source={'revision': '2'}, text='External r2')
        job = self.reserve_private_scope(parent, old, 'new-parent-external')
        result = await self.agent_command(job, child, 'uncovered-refresh', 'plan', {'source_versions': {source['id']: 2}})
        self.assertEqual(result.get('error'), 'source_basis_required', result)
        self.assertEqual(self.service.get_item(child['id']), child)

    async def test_human_material_and_position_survive_dependency_maintenance(self):
        source, child, old = await self.scenario()
        child = self.service.execute('felix', {'operation_id': 'human-position', 'action': 'plan',
            'item_id': child['id'], 'expected_version': child['version'],
            'fields': {'decision_needed': True, 'decision_question': 'Room remains my decision'}})['item']
        child = self.service.execute('felix', {'operation_id': 'human-material', 'action': 'put_material',
            'item_id': child['id'], 'expected_version': child['version'],
            'fields': {'content': 'Maximum 12; two facilitators; no sales'}})['item']
        original_materials = child['materials']
        job = self.reserve_private_scope(source, old, 'new-parent-human')
        result = await self.agent_command(job, child, 'refresh-preserve-human', 'plan', {'source_versions': {source['id']: 2}})
        self.assertEqual(result['status'], 'applied', result)
        self.assertEqual(result['item']['materials'], original_materials)
        self.assertEqual(result['item']['decision_question'], 'Room remains my decision')
        self.assertTrue(result['item']['decision_needed'])
