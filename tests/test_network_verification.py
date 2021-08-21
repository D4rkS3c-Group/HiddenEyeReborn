import unittest
from hiddeneye_reborn.network.verification import verify_connection

class ConnectionControllerTests(unittest.TestCase):
    def test_verify_connection(self):
        self.assertTrue(verify_connection(url="https://google.com"))
        self.assertTrue(verify_connection(url="https://firefox.com"))
        self.assertTrue(verify_connection(url="https://github.com"))
        self.assertTrue(verify_connection(url="https://google.com", timeout=11.11))
        self.assertTrue(verify_connection(url="https://firefox.com", timeout=12.22))
        self.assertTrue(verify_connection(url="https://github.com", timeout=13.33))
        self.assertFalse(verify_connection(url="https://asdasdasdsad.com"))
        self.assertFalse(verify_connection(url="https://ffftgrrererer.com"))
        self.assertFalse(verify_connection(url="https://git1svnhsdsgthr.com"))
        self.assertFalse(verify_connection(url="https://asdasdasdsad.com", timeout=11.11))
        self.assertFalse(verify_connection(url="https://ffftgrrererer.com", timeout=12.22))
        self.assertFalse(verify_connection(url="https://git1svnhsdsgthr.com", timeout=13.33))
if __name__ == '__main__':
    unittest.main()
