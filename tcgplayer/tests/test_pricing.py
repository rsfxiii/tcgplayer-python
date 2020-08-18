import unittest

from src.api.pricing import Pricing, MarketPrice, ProductPrice, BuylistPrice


class PricingTestCase(unittest.TestCase):
    def test_endpoint(self):
        expected = '/pricing'
        self.assertEqual(Pricing.endpoint, expected)

    def test_base_url(self):
        expected = 'https://api.tcgplayer.com/pricing'
        self.assertEqual(Pricing.base_url, expected)


class MarketPriceTestCase(unittest.TestCase):
    def test_endpoint(self):
        expected = '/marketprices'
        self.assertEqual(MarketPrice.endpoint, expected)

    def test_get_by_sku(self):
        expected = 'https://api.tcgplayer.com/pricing/marketprices/1'
        self.assertEqual(MarketPrice.get_by_sku(1), expected)

    def test_list_by_skus(self):
        expected = 'https://api.tcgplayer.com/pricing/sku/1,2,3'
        self.assertEqual(MarketPrice.list_by_skus([1,2,3]), expected)


class ProductPriceTestCase(unittest.TestCase):
    def test_list_by_group(self):
        expected = 'https://api.tcgplayer.com/pricing/group/1'
        self.assertEqual(ProductPrice.list_by_group(1), expected)

    def test_list_by_id(self):
        expected = 'https://api.tcgplayer.com/pricing/product/1'
        self.assertEqual(ProductPrice.list_by_id(1), expected)

    def test_list_by_ids(self):
        expected = 'https://api.tcgplayer.com/pricing/product/1,2,3'
        self.assertEqual(ProductPrice.list_by_id([1,2,3]), expected)


class BuylistPriceTestCase(unittest.TestCase):
    def test_list_by_products(self):
        expected = 'https://api.tcgplayer.com/pricing/buy/product/1,2,3'
        self.assertEqual(BuylistPrice.list_by_products([1,2,3]), expected)

    def test_list_by_skus(self):
        expected = 'https://api.tcgplayer.com/pricing/buy/sku/1,2,3'
        self.assertEqual(BuylistPrice.list_by_skus([1,2,3]), expected)

    def test_list_by_group(self):
        expected = 'https://api.tcgplayer.com/pricing/buy/group/1'
        self.assertEqual(BuylistPrice.list_by_group(1), expected)
