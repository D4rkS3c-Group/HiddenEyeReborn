import unittest
from hiddeneye_reborn.network.installation import is_dependency_installed

class NetworkInstallationTests(unittest.TestCase):
    def test_check_dependency(self):
        self.assertTrue(is_dependency_installed(name='echo'))
        self.assertTrue(is_dependency_installed(name='pwd'))
        self.assertTrue(is_dependency_installed(name='which'))
        self.assertTrue(is_dependency_installed(name='kill'))
        self.assertTrue(is_dependency_installed(name='test'))
        self.assertFalse(is_dependency_installed(name='qwe123!@#QWE'))
        self.assertFalse(is_dependency_installed(name='ewq321EWQ#@!'))
        self.assertFalse(is_dependency_installed(name='!@#$%^&*!@#%^'))
        self.assertFalse(is_dependency_installed(name='qlrjngejrgnej'))
        self.assertFalse(is_dependency_installed(name='sjlfbnsfklnji'))