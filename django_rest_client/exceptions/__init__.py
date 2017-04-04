import json

import requests


ALLOWED_HTTP_METHODS = frozenset(('GET', 'POST', 'PUT', 'DELETE', 'PATCH'))


class Client(object):
    _base_url = None
    _timeout = 3
    _parser = staticmethod(json.loads)

    def __init__(self, profile, **kwargs):
        pass

    def _rest_call(self, url, method='GET', **kwargs):
        pass