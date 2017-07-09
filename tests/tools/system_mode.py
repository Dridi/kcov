import testbase
import os
import time
import unittest
import parse_cobertura

class SystemModeBase(testbase.KcovTestCase):
    def writeToPipe(self, str):
        f = open("/tmp/kcov-system.pipe", "w")
        f.write(str)
        f.close()

class system_mode_can_start_and_stop_daemon(SystemModeBase):
    def runTest(self):
        self.setUp()
        rv,o = self.do(testbase.kcov_system_daemon + " -d", False)

        pf = "/tmp/kcov-system.pid"
        assert os.path.isfile(pf)

        self.writeToPipe("STOPME")

        time.sleep(2)
        
        assert os.path.isfile(pf) == False
