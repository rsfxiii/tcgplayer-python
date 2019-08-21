from tcgplayer.src.api.client import TCGPlayer, Client

import unittest


class TestClient(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        self.client.read_config('config.ini', 'Default')
        self.tcg_client = TCGPlayer(self.client)

    def test_client_exists(self):
        self.assertIsNotNone(self.client)

    def test_base_url(self):
        self.assertEqual(self.tcg_client.base_url, 'https://api.tcgplayer.com')

    def test_initial_session(self):
        self.assertIsNotNone(self.client._session)
        self.assertEqual(self.client._session, {'obj': None, 'access': None})

    def test_read_config(self):
        self.assertIsNotNone(self.client._config['parser'])
        self.assertIsNotNone(self.client._config['data'])

    def test_refresh_access(self):
        self.client.refresh_access(self.tcg_client.refresh_url)
        self.assertIsNotNone(self.client._session['access'])

    def test_authorize_session(self):
        self.client.refresh_access(self.tcg_client.refresh_url)
        self.client.authorize_session()
        # Assert changes in the session auth header
        self.assertIn('Authorization', self.client._session['obj'].headers)
        self.assertIn('Bearer', self.client._session['obj'].headers['Authorization'])
