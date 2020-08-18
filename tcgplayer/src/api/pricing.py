from .base import TCGPlayer
from ..helpers import convert_list_to_string


class Pricing(object):
    endpoint = '/pricing'
    base_url = TCGPlayer.api_url + endpoint


class MarketPrice(object):
    endpoint = '/marketprices'
    base_url = Pricing.base_url + endpoint

    @staticmethod
    def get_by_sku(sku_id):
        return f"{MarketPrice.base_url}/{sku_id}"

    @staticmethod
    def list_by_skus(sku_ids):
        arg_string = convert_list_to_string(sku_ids)
        return f"{Pricing.base_url}/sku/{arg_string}"


class ProductPrice(object):
    """ Uses base pricing endpoint """
    @staticmethod
    def list_by_group(group_ids):
        arg_string = convert_list_to_string(group_ids)
        return f"{Pricing.base_url}/group/{arg_string}"

    @staticmethod
    def list_by_id(product_ids):
        arg_string = convert_list_to_string(product_ids)
        return f"{Pricing.base_url}/product/{arg_string}"


class BuylistPrice(object):
    endpoint = '/buy'
    base_url = Pricing.base_url + endpoint

    @staticmethod
    def list_by_products(product_ids):
        arg_string = convert_list_to_string(product_ids)
        return f"{BuylistPrice.base_url}/product/{arg_string}"

    @staticmethod
    def list_by_skus(sku_ids):
        arg_string = convert_list_to_string(sku_ids)
        return f"{BuylistPrice.base_url}/sku/{arg_string}"

    @staticmethod
    def list_by_group(group_id):
        return f"{BuylistPrice.base_url}/group/{group_id}"
