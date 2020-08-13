import unittest

from src.api.endpoints import TCGPlayer, Catalog, Category, Group


class TCGPlayerTestCase(unittest.TestCase):
    def test_is_imported(self):
        self.assertIsNotNone(TCGPlayer)

    def test_api_url(self):
        result = TCGPlayer.api_url
        self.assertEqual(result, 'https://api.tcgplayer.com')

