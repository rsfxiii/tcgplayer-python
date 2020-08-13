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
    def get_details(category_id):
        return f"{Category.base_url}/{category_id}"

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
    def get_details(group_id):
        return f"{Group.base_url}/{group_id}"

    @staticmethod
    def get_media(group_id):
        return f"{Group.base_url}/{group_id}/media"

    @staticmethod
    def list_details():
        return Group.base_url
