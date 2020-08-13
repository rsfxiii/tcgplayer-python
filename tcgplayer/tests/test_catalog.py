import unittest

from src.api.endpoints import Catalog, Category, Group


class CatalogTestCase(unittest.TestCase):
    def test_is_imported(self):
        self.assertIsNotNone(Catalog)

    def test_endpoint(self):
        expected = '/catalog'
        self.assertEqual(Catalog.endpoint, expected)

    def test_base_url(self):
        expected = 'https://api.tcgplayer.com/catalog'
        self.assertEqual(Catalog.base_url, expected)


class CategoryTestCase(unittest.TestCase):
    def test_is_imported(self):
        self.assertIsNotNone(Category)

    def test_endpoint(self):
        expected = '/categories'
        self.assertEqual(Category.endpoint, expected)

    def test_base_url(self):
        expected = 'https://api.tcgplayer.com/catalog/categories'
        self.assertEqual(Category.base_url, expected)

    def test_list(self):
        expected = 'https://api.tcgplayer.com/catalog/categories'
        self.assertEqual(Category.list(), expected)

    def test_get_details(self):
        expected = 'https://api.tcgplayer.com/catalog/categories/1'
        self.assertEqual(Category.get_details(1), expected)

    def test_get_search_manifest(self):
        expected = 'https://api.tcgplayer.com/catalog/categories/1/search/manifest'
        self.assertEqual(Category.get_search_manifest(1), expected)

    # TODO: Figure out what params could passed for this
    def test_search_products(self):
        pass

    def test_get_groups(self):
        expected = 'https://api.tcgplayer.com/catalog/categories/1/groups'
        self.assertEqual(Category.get_groups(1), expected)

    def test_get_printings(self):
        expected = 'https://api.tcgplayer.com/catalog/categories/1/printings'
        self.assertEqual(Category.get_printings(1), expected)

    def test_get_rarities(self):
        expected = 'https://api.tcgplayer.com/catalog/categories/1/rarities'
        self.assertEqual(Category.get_rarities(1), expected)

    def test_get_conditions(self):
        expected = 'https://api.tcgplayer.com/catalog/categories/1/conditions'
        self.assertEqual(Category.get_conditions(1), expected)

    def test_get_languages(self):
        expected = 'https://api.tcgplayer.com/catalog/categories/1/languages'
        self.assertEqual(Category.get_languages(1), expected)

    def test_get_media(self):
        expected = 'https://api.tcgplayer.com/catalog/categories/1/media'
        self.assertEqual(Category.get_media(1), expected)


class GroupTestCase(unittest.TestCase):
    def test_is_imported(self):
        self.assertIsNotNone(Group)

    def test_endpoint(self):
        expected = '/groups'
        self.assertEqual(Group.endpoint, expected)

    def test_base_url(self):
        expected = 'https://api.tcgplayer.com/catalog/groups'
        self.assertEqual(Group.base_url, expected)

    # TODO: Add test for list of strings argument
    def test_get_details(self):
        expected = 'https://api.tcgplayer.com/catalog/groups/1'
        self.assertEqual(Group.get_details(1), expected)

    def test_list_details(self):
        expected = 'https://api.tcgplayer.com/catalog/groups'
        self.assertEqual(Group.list_details(), expected)

    def test_get_media(self):
        expected = 'https://api.tcgplayer.com/catalog/groups/1/media'
        self.assertEqual(Group.get_media(1), expected)


class ProductTestCase(unittest.TestCase):
    def test_is_imported(self):
        self.assertIsNotNone(Product)

    def test_endpoint(self):
        expected = '/products'
        self.assertEqual(Product.endpoint, expected)

    def test_base_url(self):
        expected = 'https://api.tcgplayer.com/catalog/products'
        self.assertEqual(Product.base_url, expected)

    # TODO: Test for handling of query string params
    def test_list(self):
        expected = 'https://api.tcgplayer.com/catalog/products'
        self.assertEqual(Product.list(), expected)

    def test_get_details(self):
        expected = 'https://api.tcgplayer.com/catalog/products'
        self.assertEqual(Product.get_details(1), expected)

    def test_get_details_by_gtin(self):
        expected = 'https://api.tcgplayer.com/catalog/products/gtin/1'
        self.assertEqual(Product.get_details_by_gtin(1), expected)

    def test_list_skus(self):
        expected = 'https://api.tcgplayer.com/catalog/products/1/skus'
        self.assertEqual(Product.get_list_skus(1), expected)

    def test_list_related_products(self):
        expected = 'https://api.tcgplayer.com/catalog/products/1/productsalsopurchased'
        self.assertEqual(Product.list_related_products(1), expected)

    def test_list_media_types(self):
        expected = 'https://api.tcgplayer.com/catalog/products/1/media'
        self.assertEqual(Product.list_media_types(1), expected)


@unittest.skip
class SKUTestCase(unittest.TestCase):
    def test_is_imported(self):
        self.assertIsNotNone(SKU)

    def test_endpoint(self):
        expected = '/skus'
        self.assertEqual(SKU.endpoint, expected)

    def test_base_url(self):
        expected = 'https://api.tcgplayer.com/catalog/skus'
        self.assertEqual(SKU.base_url, expected)

    # TODO: Test for list of strings as args
    def test_get_details(self):
        expected = 'https://api.tcgplayer.com/catalog/skus/1'
        self.assertEqual(SKU.get_details(1), expected)


@unittest.skip
class ConditionTestCase(unittest.TestCase):
    def test_is_imported(self):
        self.assertIsNotNone(Condition)

    def test_endpoint(self):
        expected = '/conditions'
        self.assertEqual(Condition.endpoint, expected)

    def test_base_url(self):
        expected = 'https://api.tcgplayer.com/catalog/conditions'
        self.assertEqual(Condition.base_url, expected)

    def test_list(self):
        expected = 'https://api.tcgplayer.com/catalog/conditions'
        self.assertEqual(Condition.list(), expected)
