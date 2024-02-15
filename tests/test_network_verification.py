import unittest
from hiddeneye_reborn.network.verification import verify_connection

DEFAULT_TIMEOUT = 10
TEST_CASES_TRUE = [
    "https://google.com",
    "https://firefox.com",
    "https://github.com",
]

TEST_CASES_FALSE = [
    "https://asdasdasdsad.com",
    "https://ffftgrrererer.com",
    "https://git1svnhsdsgthr.com",
    "https://10.255.255.1",
    "https://google",    # missing domain
    "google.com",        # missing protocol
    "",                  # empty string
    "ftp://github.com",  # non-http/https URL
]


class NetworkVerificationTests(unittest.TestCase):
    def test_verify_connection(self):
        for url in TEST_CASES_TRUE:
            with self.subTest(url=url):
                self.assertTrue(verify_connection(url))

        for url in TEST_CASES_FALSE:
            with self.subTest(url=url):
                self.assertFalse(verify_connection(url))


if __name__ == "__main__":
    unittest.main()