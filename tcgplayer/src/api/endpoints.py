class TCGPlayer(object):
    api_url = 'https://api.tcgplayer.com'


class Catalog(object):
    endpoint = '/catalog'
    base_url = TCGPlayer.api_url + endpoint


class Category(object):
    endpoint = '/categories'
    base_url = Catalog.base_url + endpoint

    @staticmethod
    def list():
        return Category.base_url

    @staticmethod
    def get_details(category_ids):
        """ Accepts a string, or list of strings """
        # TODO: Convert list of strings to comma-delimited string
        return f"{Category.base_url}/{category_ids}"

    @staticmethod
    def get_search_manifest(category_id):
        return f"{Category.base_url}/{category_id}/search/manifest"

    @staticmethod
    def search_products(category_id, params):
        return

    @staticmethod
    def get_groups(category_id):
        return f"{Category.base_url}/{category_id}/groups"

    @staticmethod
    def get_printings(category_id):
        return f"{Category.base_url}/{category_id}/printings"

    @staticmethod
    def get_rarities(category_id):
        return f"{Category.base_url}/{category_id}/rarities"

    @staticmethod
    def get_conditions(category_id):
        return f"{Category.base_url}/{category_id}/conditions"

    @staticmethod
    def get_languages(category_id):
        return f"{Category.base_url}/{category_id}/languages"

    @staticmethod
    def get_media(category_id):
        return f"{Category.base_url}/{category_id}/media"


class Group(object):
    endpoint = '/groups'
    base_url = Catalog.base_url + endpoint

    @staticmethod
    def get_details(group_ids):
        """ Accepts a string, or list of strings """
        # TODO: Convert list of strings to comma-delimited string
        return f"{Group.base_url}/{group_ids}"

    @staticmethod
    def get_media(group_id):
        return f"{Group.base_url}/{group_id}/media"

    @staticmethod
    def list_details():
        return Group.base_url


class Product(object):
    endpoint = '/products'
    base_url = Catalog.base_url + endpoint

    @staticmethod
    def list():
        return Product.base_url

    @staticmethod
    def get_details(product_ids):
        """ Accepts a string, or list of strings """
        # TODO: Convert list of strings to comma-delimited string
        return f"{Product.base_url}/{product_ids}"

    @staticmethod
    def get_details_by_gtin(gtin):
        return f"{Product.base_url}/gtin/{gtin}"

    @staticmethod
    def list_skus(product_id):
        return f"{Product.base_url}/{product_id}/skus"

    @staticmethod
    def list_related_products(product_id):
        return f"{Product.base_url}/{product_id}/productsalsopurchased"

    @staticmethod
    def list_media(product_id):
        return f"{Product.base_url}/{product_id}/media"


class SKU(object):
    endpoint = '/skus'
    base_url = Catalog.base_url + endpoint

    @staticmethod
    def get_details(sku_ids):
        """ Accepts a string, or list of strings """
        # TODO: Convert list of strings to comma-delimited string
        return f"{SKU.base_url}/{sku_ids}"


class Condition(object):
    endpoint = '/conditions'
    base_url = Catalog.base_url + endpoint

    @staticmethod
    def list():
        return Condition.base_url
