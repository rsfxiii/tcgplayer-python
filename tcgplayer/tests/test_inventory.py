import unittest


from src.api.inventory import Inventory, ProductList


class InventoryTestCase(unittest.TestCase):
    def test_endpoint(self):
        expected = '/inventory'
        self.assertEqual(Inventory.endpoint, expected)

    def test_base_url(self):
        expected = 'https://api.tcgplayer.com/inventory'
        self.assertEqual(Inventory.base_url, expected)


class ProductListTestCase(unittest.TestCase):
    def test_get(self):
        expected = 'https://api.tcgplayer.com/inventory/productlists/1'
        self.assertEqual(ProductList.get(1), expected)

    def test_get_by_key(self):
        expected = 'https://api.tcgplayer.com/inventory/productlists/test'
        self.assertEqual(ProductList.get_by_key('test'), expected)

    def test_list(self):
        expected = 'https://api.tcgplayer.com/inventory/productlists'
        self.assertEqual(ProductList.list(), expected)

    def test_create(self):
        expected = 'https://api.tcgplayer.com/inventory/productlists'
        self.assertEqual(ProductList.create({}), expected)
