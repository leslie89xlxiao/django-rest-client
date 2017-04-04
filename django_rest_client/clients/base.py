import logging
import json

import requests

logger = logging.getLogger('django_rest_client')

ALLOWED_HTTP_METHODS = frozenset(('GET', 'POST', 'PUT', 'DELETE', 'PATCH'))


class Client(object):
    _base_url = None
    _timeout = 3
    _parser = staticmethod(json.loads)

    def __init__(self, profile, **kwargs):
        response = requests.requests()

    def _rest_call(self, url, method='GET', **kwargs):
        if method in ALLOWED_HTTP_METHODS:
            pass
        else:
            raise Exception( 'Invalid method "{}" is used for the HTTP request. Can only'
                'use the following: {!s}'.format(method, ALLOWED_HTTP_METHODS))

        if 200 <= response.status_code < 300:
