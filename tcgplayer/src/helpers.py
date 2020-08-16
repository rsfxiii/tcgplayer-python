import urllib.parse as urlparse
from urllib.parse import urlencode


def encode_query_params(url, params):
    parts = list(urlparse.urlparse(url))
    query = dict(urlparse.parse_qs(parts[4]))
    query.update(params)
    parts[4] = urlencode(query)
    return urlparse.urlunparse(parts)


def convert_list_to_string(list_arg, sep=","):
    raise NotImplemented
