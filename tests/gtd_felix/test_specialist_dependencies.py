"""Explicit specialist dependencies invalidate returns without granting scope."""
import copy
import unittest
from unittest.mock import patch

import test_control as fixture


class SpecialistDependenciesTests(unittest.TestCase):
    setUp = fixture.ControlTest.setUp
    tearDown = fixture.ControlTest.tearDown
    request = fixture.ControlTest.request
    reserve = fixture.ControlTest.reserve

    def command(self, item_id, action, **fields):
        self.counter = getattr(self, 'counter', 0) + 1
        item = self.service.get_item(item_id)
        receipt = self.service.execute('felix', dict(
            operation_id=f'command-{self.counter}', action=action,
            item_id=item_id, expected_version=item['version'], fields=fields))
        self.assertEqual(receipt['status'], 'applied', receipt)
        return receipt['item']

    def action(self, title, **fields):
        return self.command(self.item['id'], 'derive', kind='action', title=title,
            capability='local_work', mandate_id=self.mandate, **fields)['id']

    def job(self, item_id, **fields):
        return self.reserve('reserve-' + item_id, item_id=item_id,
            expected_version=self.service.get_item(item_id)['version'],
            max_cost_usd=1, **fields)

    def test_transitive_correction_and_undo_remain_stale_after_reopen(self):
        a = self.action('A', text='12 people')
        b = self.action('B', depends_on=[a])
        c = self.action('C', depends_on=[b])
        job = self.job(c)
        reserved = copy.deepcopy(self.control.get_job(job)['source_bases'])
        self.assertTrue({a, b}.issubset(reserved))
        self.command(a, 'edit', text='20 people')
        self.assertEqual(self.control.validate(job, 'local_work')['reason'], 'source_version_stale')
        self.command(a, 'edit', text='12 people')
        self.assertNotEqual(self.control._basis(a), reserved[a])
        for _ in range(2):
            self.service.close()
            self.service = fixture.GTDService(self.root / 'data')
            self.control = fixture.ExecutionControl(self.service, self.config)
            self.assertEqual(self.control.get_job(job)['source_bases'], reserved)
            self.assertEqual(self.control.validate(job, 'local_work')['reason'], 'source_version_stale')

    def test_new_transitive_dependency_after_reservation_rejects_old_job(self):
        a = self.action('A')
        b = self.action('B')
        c = self.action('C', depends_on=[b])
        job = self.job(c)
        reserved = copy.deepcopy(self.control.get_job(job)['source_bases'])
        self.command(b, 'edit', depends_on=[a])
        self.assertEqual(self.control.validate(job, 'local_work')['reason'], 'source_basis_required')
        self.assertEqual(self.control.get_job(job)['source_bases'], reserved)

    def test_textual_reference_does_not_expand_scope_or_invalidate_independent_sibling(self):
        a = self.action('A')
        b = self.action('B', depends_on=[a])
        independent = self.action('Independent')
        dependent_job = self.job(b)
        independent_job = self.job(independent, scope='Use material item=' + a + ' sha256=synthetic')
        self.assertNotIn(a, self.control.get_job(independent_job)['source_bases'])
        self.assertFalse(self.control.validate_target(dependent_job, 'gtd-felix', a, 'local_work')['allowed'])
        self.command(a, 'edit', text='Owner correction')
        self.assertFalse(self.control.validate(dependent_job, 'local_work')['allowed'])
        self.assertTrue(self.control.validate(independent_job, 'local_work')['allowed'])

    def test_missing_dependency_rejects_validation_and_new_reservation(self):
        a = self.action('A')
        b = self.action('B', depends_on=[a])
        job = self.job(b)
        get_item = self.service.get_item
        with patch.object(self.service, 'get_item', side_effect=lambda item_id:
                None if item_id == a else get_item(item_id)):
            self.assertEqual(self.control.validate(job, 'local_work')['reason'], 'source_version_stale')
            result = self.control.reserve('gtd-felix', 'missing-reserve', self.request(
                item_id=b, expected_version=get_item(b)['version'], purpose='Other'))
            self.assertEqual(result['error'], 'source_version_stale')

    def test_traversal_terminates_for_cycles_across_ancestry_and_dependency(self):
        child = self.action('Child')
        job = self.job(child)
        get_item = self.service.get_item
        parent = dict(get_item(self.item['id']), depends_on=[child])
        with patch.object(self.service, 'get_item', side_effect=lambda item_id:
                parent if item_id == self.item['id'] else get_item(item_id)):
            self.assertEqual(self.control._dependencies(self.control._load(),
                self.control.get_job(job)), {self.item['id']})
