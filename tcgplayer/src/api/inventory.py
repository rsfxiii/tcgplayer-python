from .base import TCGPlayer
from ..helpers import encode_query_params


class Inventory(object):
    endpoint = '/inventory'
    base_url = TCGPlayer.api_url + endpoint


class ProductList(object):
    endpoint = '/productlists'
    base_url = Inventory.base_url + endpoint

    @staticmethod
    def get(productlist_id):
        return f"{ProductList.base_url}/{productlist_id}"

    @staticmethod
    def get_by_key(key_string):
        return f"{ProductList.base_url}/{key_string}"

    @staticmethod
    def list():
        return ProductList.base_url

    @staticmethod
    def create(payload):
        return encode_query_params(ProductList.base_url, payload)
