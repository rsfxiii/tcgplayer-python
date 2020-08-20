import unittest

from src.client import Client


class ClientTestCase(unittest.TestCase):
    def setUp(self):
        self.credentials = {
            'PUB_KEY': 'test-pub-key',
            'PRIV_KEY': 'test-priv-key'
        }

    def test_build_access_payload(self):
        expected = {
            'grant_type': 'client_credentials',
            'client_id': 'test-pub-key',
            'client_secret': 'test-priv-key'
        }
        self.assertEquals(Client.build_access_payload(self.credentials['PUB_KEY'],
                                                      self.credentials['PRIV_KEY'], expected))

    # TODO: How can we test Client.refresh_access_token()?
    def test_refresh_access_token(self):
        pass

    # TODO: How can we test Client.handle_request()?
    def test_handle_request(self):
        pass
