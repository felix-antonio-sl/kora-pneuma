"""Real private user units and synthetic stdio workers; no Codex/model/auth."""
import asyncio
import hashlib
import json
import os
from pathlib import Path
import signal
import sys
import time
import unittest
import uuid
from runtime_location import RUNTIME
sys.path.insert(0,str(RUNTIME))
from gtd_felix.codex import CodexAdapter
from gtd_felix.codex_local import properties, command, identity
import test_codex as common

class LocalContainmentTests(unittest.IsolatedAsyncioTestCase):
    save=common.CodexTests.save
    reserve=common.CodexTests.reserve
    audit=common.CodexTests.audit
    asyncSetUp=common.CodexTests.asyncSetUp
    asyncTearDown=common.CodexTests.asyncTearDown

    async def test_setsid_child_closed_before_timeout_and_witness_preserved(self):
        prelude="""import subprocess,os,json
from pathlib import Path
child=subprocess.Popen([__import__('sys').executable,'-c','import threading; threading.Event().wait()'],start_new_session=True)
Path(os.environ['CODEX_HOME'],'child.json').write_text(json.dumps({'pid':child.pid,'pgid':os.getpgid(child.pid)}))
"""
        self.binary.write_text('#!'+sys.executable+'\n'+prelude+common.FAKE)
        self.adapter.config['binary_sha256']=hashlib.sha256(self.binary.read_bytes()).hexdigest()
        witness=await asyncio.create_subprocess_exec(sys.executable,'-c','import time;time.sleep(15)',start_new_session=True)
        witness_id=identity(witness.pid)
        try:
            started=time.monotonic();job=self.reserve();result=await self.adapter.submit(job,'synthetic')
            self.assertEqual(result['native_status'],'running',result)
            child=json.loads((self.home/'child.json').read_text());native=self.adapter._get('process:'+job)
            driver=self.adapter._get('driver:'+job)
            self.assertNotEqual(native['pid'],driver['pid']);self.assertEqual(child['pid'],child['pgid'])
            self.assertNotEqual(child['pgid'],native['pgid'])
            await self.adapter.stop(job);result=await self.adapter.poll(job)
            self.assertTrue(result['terminal'],result);self.assertEqual(result['native_status'],'cancelled')
            self.assertFalse(Path('/proc',str(child['pid'])).exists());self.assertFalse(Path('/proc',str(native['pid'])).exists())
            self.assertTrue(self.adapter._get('local:'+job)['contained'])
            self.assertLess(time.monotonic()-started,10)
            self.assertEqual(identity(witness.pid),witness_id)
        finally:
            if witness.returncode is None:
                self.assertEqual(identity(witness.pid),witness_id);os.killpg(witness.pid,signal.SIGTERM);await witness.wait()

    async def test_late_activation_absolute_guard_prevents_execution(self):
        marker=self.root/'must-not-exist'
        name='gtd-late-test-'+uuid.uuid4().hex
        record={'name':name,'deadline':time.time()+.8,'runtime_seconds':.3,'start_seconds':.2,'grace':.1}
        # Simulates delayed manager acceptance / lost start ACK: submit after cutoff.
        await asyncio.sleep(.3)
        p=await asyncio.create_subprocess_exec('systemd-run','--user','--quiet','--pipe','--wait','--unit='+name,
            *properties(record),sys.executable,'-c','from pathlib import Path;Path('+repr(str(marker))+').write_text("bad")',
            stdout=asyncio.subprocess.PIPE,stderr=asyncio.subprocess.DEVNULL)
        await asyncio.wait_for(p.communicate(),3)
        self.assertFalse(marker.exists())
        state=await command('systemctl','--user','show',name+'.service','--property=MainPID,ActiveState')
        self.assertIn('MainPID=0',state)

    async def test_separate_read_only_recovery_cannot_steer_or_start(self):
        job=self.reserve();await self.adapter.submit(job,'synthetic')
        old=self.adapter._get('local:'+job)
        await self.adapter.close()
        native=json.loads((self.home/'native.json').read_text());native['turns'][0]['status']='interrupted'
        (self.home/'native.json').write_text(json.dumps(native))
        self.adapter=CodexAdapter(self.control,self.config)
        result=await self.adapter.reconcile(job)
        self.assertTrue(result['terminal'],result)
        self.assertEqual(self.adapter._get('local:'+job)['unit'],old['unit'])
        self.assertEqual(sum(x['method']=='turn/start' for x in self.audit()),1)
        self.assertNotIn('thread/resume',[x['method'] for x in self.audit()])
        rows=self.service.store.db.execute("SELECT value FROM metadata WHERE key LIKE ?",('codex:local:'+job+':read:%',)).fetchall()
        self.assertEqual(len(rows),1);self.assertTrue(json.loads(rows[0][0])['read_only'])

    async def test_historical_stdio_record_is_not_assigned_a_unit(self):
        # A pre-upgrade durable record has no local_supervised flag.
        job=self.reserve()
        with self.service.store.transaction():self.adapter._put('job:'+job,{'delivery':'legacy_fixture'})
        rpc=await self.adapter._spawn(job,self.route)
        self.assertIsNotNone(rpc.process);self.assertIsNone(rpc.channel)
        self.assertIsNone(self.adapter._get('local:'+job))
        native=self.adapter._get('process:'+job)
        self.assertEqual(native['pid'],rpc.process.pid)
        await self.adapter._close_process(job)
        self.assertFalse(Path('/proc',str(native['pid'])).exists())
