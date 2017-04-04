# -*- coding: utf-8 -*-
import logging
import json
import urlparse

import requests

from ..exceptions import ConfigException, ServerResponseException
from ..models import DjangoRestClient

logger = logging.getLogger('django_rest_client')

ALLOWED_HTTP_METHODS = frozenset(('GET', 'POST', 'PUT', 'DELETE', 'PATCH'))


class Client(object):
    _config_name = None
    _base_url = None
    _timeout = 3
    _parser = staticmethod(json.loads)

    def __init__(self, profile, **kwargs):
        self.profile = profile
        self._load_config()

    def _load_config(self):
        class_name = self.__class__.__name__

        if not self._config_name:
            raise ConfigException('please set "_config_name" for setting lookup')

        rest_client = DjangoRestClient.objects.filter(
            name=self._config_name).first()

        client_config = rest_client.config if rest_client else {}

        if self.profile in client_config:
            self._config = client_config[self.profile]
        else:
            ConfigException('Configuration for {} is not found with profile {}'.format(class_name, self.profile))

        self._config['config_profile'] = self.profile
        self._config['_class'] = class_name

        self.base_url = self._build_base_url()
        self.timeout = self._config.get('TIMEOUT', self._timeout)

    def _build_base_url(self):
        hostname_urls = self.config('HOSTNAME').split('/', 1)
        port = self.config('PORT') or '80'
        base_url = "http://{}:{}".format(hostname_urls[0], port)

        if len(hostname_urls) > 1:
            base_url = urlparse.urljoin(base_url, '/'+hostname_urls[1])
        if self._base_url is not None:
            base_url = urlparse.urljoin(base_url, '/'+self._base_url)
        return base_url

    def config(self, key=None):
        return self._config if key is None else self._confg.get(key)

    def concat_url(self, url):
        return '{}/{}'.format(self.base_url, url)

    def _rest_call(self, url, method='GET', **kwargs):

        discard_error = kwargs.pop('discard_error', False)

        url = self.cancat_url(url)

        if method in ALLOWED_HTTP_METHODS:
            try:
                response = requests.request(method.lower(), url, **kwargs)
            except Exception as e:
                pass

        else:
            raise Exception( 'Invalid method "{}" is used for the HTTP request. Can only'
                'use the following: {!s}'.format(method, ALLOWED_HTTP_METHODS))

        if 200 <= response.status_code < 300:
            response_data = response.text.strip()
            return self._parser(response_data) if response_data else None
        else:
            exc_data = {
                'client': self,
                'url': url,
                'method': method,
                'kwargs': kwargs,
                'response': response
            }
            exc = ServerResponseException(**exc_data)

            if not discard_error:
                logger.exception(exc.message)

            raise exc
