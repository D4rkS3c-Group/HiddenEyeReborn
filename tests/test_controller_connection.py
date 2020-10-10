import unittest
from hiddeneye_reborn.controllers.controller_connection import ConnectionController


class ConnectionControllerTests(unittest.TestCase):
    def test_verify_connection(self):
        self.assertTrue(ConnectionController(host="https://google.com").verify_connection())
        self.assertTrue(ConnectionController(host="https://firefox.com").verify_connection())
        self.assertTrue(ConnectionController(host="https://youtube.com").verify_connection())


if __name__ == '__main__':
    unittest.main()
