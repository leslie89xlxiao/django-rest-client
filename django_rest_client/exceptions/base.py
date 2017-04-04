import json


class RestClientException(Exception):
    pass


class ConfigException(RestClientException):
    pass


class InvalidRestMethodException(RestClientException):
    pass


class ServerResponseException(RestClientException):

    def __init__(self, **kwargs):
        self.client = kwargs.get('client', None)
        self.url = kwargs.get('url', None)
        self.method = kwargs.get('method', None)
        self.kwargs = kwargs.get('kwargs', None)
        self.response = kwargs.get('response', None)

    def __str__(self):
        msg = {
            'request': {
                'client': self.client.__class__.__name__,
                'url': self.url,
                'headers': self.response.headers,
                'method': self.method,
                'kwargs': self.kwargs
            },
            'response': {
                'text': self.response.text
            }
        }

        return u'Server response not OK. Detail: {}'.format(json.dumps(msg))
