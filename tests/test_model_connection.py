import unittest
import hiddeneye_reborn.models.model_connection as model_connection


class ConnectionModelTests(unittest.TestCase):
    def test_host_setter(self):
        host_for_test = "https://firefox.com"
        print(f"New host is {host_for_test}, old host was {model_connection.ConnectionModel().host}")
        new_host = model_connection.ConnectionModel().host = host_for_test
        print(f"Successfully set host to {new_host}")
        self.assertEqual(new_host, host_for_test)

    def test_host_getter(self):
        self.assertEqual(model_connection.ConnectionModel().host, "https://google.com")
        print(f"Getter returns {model_connection.ConnectionModel().host}")


if __name__ == '__main__':
    unittest.main()
