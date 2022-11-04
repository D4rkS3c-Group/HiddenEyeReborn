import unittest
from hiddeneye_reborn.network.installation import check_dependency

class NetworkInstallationTests(unittest.TestCase):
    def test_check_dependency(self):
        self.assertTrue(check_dependency(name='echo'))
        self.assertTrue(check_dependency(name='pwd'))
        self.assertTrue(check_dependency(name='which'))
        self.assertTrue(check_dependency(name='kill'))
        self.assertTrue(check_dependency(name='test'))
        self.assertFalse(check_dependency(name='qwe123!@#QWE'))
        self.assertFalse(check_dependency(name='ewq321EWQ#@!'))
        self.assertFalse(check_dependency(name='!@#$%^&*!@#%^'))
        self.assertFalse(check_dependency(name='qlrjngejrgnej'))
        self.assertFalse(check_dependency(name='sjlfbnsfklnji'))