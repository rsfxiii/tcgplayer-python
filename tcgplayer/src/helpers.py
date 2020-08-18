import urllib.parse as urlparse
from urllib.parse import urlencode


def encode_query_params(url, params):
    """ Returns URL with query string attached to it """
    parts = list(urlparse.urlparse(url))
    query = dict(urlparse.parse_qs(parts[4]))
    query.update(params)
    parts[4] = urlencode(query)
    return urlparse.urlunparse(parts)


def convert_list_to_string(list_arg, sep=","):
    """ Items must be a string or integer, they are cast to string before storage"""
    """ Items can also not be falsey, so 0 and '' would be stripped, hence "and x" """
    if type(list_arg) is str:
        return list_arg

    if type(list_arg) is int:
        return str(list_arg)

    try:
        accepted = [str(x) for x in list_arg if (type(x) in [str, int] and x)]
        return sep.join(accepted.__iter__())
    except TypeError:
        raise
