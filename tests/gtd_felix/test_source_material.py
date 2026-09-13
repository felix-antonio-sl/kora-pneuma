"""Identified collateral copy through authenticated HTTP/MCP, real Store."""
import hashlib
import unittest
from unittest.mock import patch
import test_application as http
from test_material_files import pptx, fields
from gtd_felix.mcp import MCPClient
from gtd_felix.service import GTDService

class SourceMaterialTests(unittest.IsolatedAsyncioTestCase):
    asyncSetUp=http.HTTPTests.asyncSetUp
    asyncTearDown=http.HTTPTests.asyncTearDown
    private_job=http.HTTPTests.private_job
    reserve_private_scope=http.HTTPTests.reserve_private_scope
    finish_scope_job=http.HTTPTests.finish_scope_job
    agent_command=http.HTTPTests.agent_command

    async def setup_copy(self):
        root,old=self.private_job()
        payload=pptx()
        seeded=self.service.execute('felix',{'operation_id':'seed','action':'put_material','item_id':root['id'],
            'expected_version':root['version'],'fields':fields(payload)})['item']
        self.finish_scope_job(old)
        job=self.reserve_private_scope(seeded,old,'fresh')
        child=(await self.agent_command(job,seeded,'derive','derive',{'kind':'action','title':'Use supplied collateral','capability':'prepare_private'}))['item']
        m=seeded['materials'][0]
        ref={'item_id':root['id'],'material_id':m['id'],'version':m['version'],'sha256':m['original']['sha256']}
        return seeded,child,job,ref,payload

    async def test_pptx_copy_mcp_provenance_replay_and_restore(self):
        root,child,job,ref,payload=await self.setup_copy()
        client=MCPClient(self.url,http.PRINCIPAL)
        command={'operation_id':'copy','action':'put_material','item_id':child['id'],'expected_version':child['version'],
            'fields':{'source_material':ref,'title':'Selected collateral'}}
        result=await client.call('gtd_command',{'job_id':job,'command':command})
        self.assertEqual(result['status'],'applied',result)
        material=result['item']['materials'][-1]
        self.assertEqual(material['source_material']['author'],'felix')
        self.assertEqual(material['author'],'gtd-felix')
        self.assertEqual(self.service.read_material_file(child['id'],material['id'],1)['data'],payload)
        self.assertEqual((await client.call('gtd_command',{'job_id':job,'command':command}))['status'],'already_applied')
        archive=self.service.data_dir.parent/'copy-export.zip';self.service.export(archive)
        restored=GTDService.restore(archive,self.service.data_dir.parent/'restored-copy')
        try:
            self.assertTrue(restored.recovery_required)
            self.assertEqual(restored.read_material_file(child['id'],material['id'],1)['data'],payload)
            self.assertEqual(restored.get_item(child['id'])['materials'],result['item']['materials'])
        finally:restored.close()

    async def test_outside_scope_and_protected_destination_reject_before_bytes(self):
        root,child,job,ref,_=await self.setup_copy()
        outsider=self.service.capture('felix','outside','Unrelated collateral')['item']
        for source in ({**ref,'item_id':outsider['id']},):
            with patch.object(self.service,'read_material_file',side_effect=AssertionError('unauthorized bytes')):
                result=await self.agent_command(job,child,'outside-copy','put_material',{'source_material':source})
            self.assertEqual(result.get('error'),'outside_job_scope',result)
        owned=self.service.execute('felix',{'operation_id':'human-child-material','action':'put_material','item_id':child['id'],
            'expected_version':child['version'],'fields':{'content':'Human protected content'}})['item']
        self.finish_scope_job(job);job=self.reserve_private_scope(root,job,'after-human-material')
        with patch.object(self.service,'read_material_file',side_effect=AssertionError('protected destination bytes')):
            result=await self.agent_command(job,owned,'overwrite-human','put_material',{'source_material':ref,'material_id':owned['materials'][0]['id']})
        self.assertEqual(result.get('error'),'human_material_protected',result)
        self.assertEqual(self.service.get_item(child['id']),owned)

    async def test_false_hash_and_exclusive_content_reject_before_bytes(self):
        root,child,job,ref,_=await self.setup_copy()
        for n,values in enumerate(({'source_material':{**ref,'sha256':'0'*64}},
                {'source_material':ref,'content':'cannot substitute'}, {'source_material':ref,'filename':'override.pptx'},
                {'source_material':ref,'mime_type':'text/plain'})):
            with patch.object(self.service,'read_material_file',side_effect=AssertionError('invalid bytes')):
                result=await self.agent_command(job,child,'bad-copy-'+str(n),'put_material',values)
            self.assertEqual(result['status'],'rejected',result)
        self.assertEqual(self.service.get_item(child['id']),child)

    async def test_source_edit_invalidates_copy_and_cannot_wash_dependency(self):
        root,child,job,ref,_=await self.setup_copy()
        result=await self.agent_command(job,child,'copy','put_material',{'source_material':ref})
        self.assertEqual(result['status'],'applied',result)
        self.assertTrue(self.service.materials(child['id'])[0]['valid'])
        self.service.revise_source('felix','changed-root-source',root['id'],source={'revision':2},text='Corrected evidence')
        self.assertFalse(self.service.materials(child['id'])[0]['valid'])
        current=self.service.get_item(child['id'])
        self.finish_scope_job(job);fresh_root=self.service.get_item(root['id'])
        job=self.reserve_private_scope(fresh_root,job,'new-revision-job')
        with patch.object(self.service,'read_material_file',side_effect=AssertionError('old material bytes')):
            result=await self.agent_command(job,current,'wash-old','put_material',{'source_material':ref,'source_versions':{root['id']:2}})
        self.assertEqual(result.get('error'),'source_material_not_current',result)

    async def test_superseded_source_invalidates_copies_transitively(self):
        root,child,job,ref,_=await self.setup_copy()
        first=await self.agent_command(job,child,'copy-one','put_material',{'source_material':ref})
        self.assertEqual(first['status'],'applied',first)
        copied=first['item']['materials'][-1]
        second_ref={'item_id':child['id'],'material_id':copied['id'],'version':1,'sha256':ref['sha256']}
        second=await self.agent_command(job,first['item'],'copy-two','put_material',{'source_material':second_ref})
        self.assertEqual(second['status'],'applied',second)
        self.assertEqual(second['item']['materials'][-1]['source_material']['author'],'gtd-felix')
        self.assertTrue(all(m['valid'] for m in self.service.materials(child['id'])))
        self.service.execute('felix',{'operation_id':'replacement-collateral','action':'put_material','item_id':root['id'],
            'expected_version':self.service.get_item(root['id'])['version'],
            'fields':{**fields(pptx('Updated collateral')),'material_id':ref['material_id']}})
        self.assertTrue(all(not m['valid'] for m in self.service.materials(child['id'])))

    async def test_corrupt_original_fails_existing_reader_without_copy(self):
        root,child,job,ref,_=await self.setup_copy()
        original=self.service.data_dir/root['materials'][0]['original']['path']
        original.write_bytes(b'corrupt')
        result=await self.agent_command(job,child,'corrupt-copy','put_material',{'source_material':ref})
        self.assertEqual(result['status'],'rejected',result)
        self.assertEqual(self.service.get_item(child['id']),child)

    async def test_authentic_executor_material_can_be_reused_and_revocation_propagates(self):
        root,child,job,_,_=await self.setup_copy()
        self.finish_scope_job(job)
        clarified=self.service.execute('felix',{'operation_id':'owner-project','action':'clarify','item_id':root['id'],
            'expected_version':self.service.get_item(root['id'])['version'],
            'fields':{'kind':'project','commitment':'committed','completion_criteria':'Prepare private collateral'}})
        self.assertEqual(clarified['status'],'applied',clarified)
        grant=self.service.execute('felix',{'operation_id':'executor-mandate','action':'grant_mandate','item_id':root['id'],
            'expected_version':self.service.get_item(root['id'])['version'],'fields':{'scope_item_id':root['id'],
                'capabilities':['prepare_private'],'actors':['worker'],'completion_criteria':'Prepare private collateral'}})
        self.assertEqual(grant['status'],'applied',grant)
        mandate=grant['mandate']['id']
        provided=self.service.execute('worker',{'operation_id':'executor-file','action':'put_material','item_id':root['id'],
            'expected_version':grant['item']['version'],'fields':{**fields(pptx('Executor content')),'mandate_id':mandate}})
        self.assertEqual(provided['status'],'applied',provided)
        m=provided['item']['materials'][-1]
        ref={'item_id':root['id'],'material_id':m['id'],'version':1,'sha256':m['original']['sha256']}
        job=self.reserve_private_scope(provided['item'],job,'principal-after-executor')
        result=await self.agent_command(job,child,'reuse-executor','put_material',{'source_material':ref})
        self.assertEqual(result['status'],'applied',result)
        self.assertEqual(result['item']['materials'][-1]['source_material']['author'],'worker')
        self.assertTrue(self.service.materials(child['id'])[-1]['valid'])
        revoked=self.service.execute('felix',{'operation_id':'revoke-executor','action':'revoke_mandate','item_id':root['id'],
            'expected_version':self.service.get_item(root['id'])['version'],'fields':{'mandate_id':mandate}})
        self.assertEqual(revoked['status'],'applied',revoked)
        self.assertFalse(self.service.materials(child['id'])[-1]['valid'])
