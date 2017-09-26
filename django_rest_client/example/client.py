from django_rest_client.clients import JSONClient, RestClientFactory
from .exception import ExampleClientError


class Example(JSONClient):
    _config_name = 'EXAMPLE'
    _default_profile = 'default'
    _base_url_path = ''
    _default_timeout = 3
    _exception_class = ExampleClientError

    def mock_get_request(self):
        url = 'mock_get_request?name={}&age={}'.format('leslie89xlxiao', 20)
        return self._rest_call(url, 'GET')

    def mock_post_request(self, name, age):
        url = 'mock_post_request'
        data = {
            'name': name,
            'age': age
        }
        return self._rest_call(url, 'POST', data=data)

    def mock_delete_request(self, delete_id):
        url = 'mock_delete_request/{}'.format(delete_id)
        return self._rest_call(url, 'DELETE')

    def mock_put_request(self, name, age):
        url = 'mock_put_request'
        data = {
            'name': name,
            'age': age
        }
        return self._rest_call(url, 'PUT', data=data)

    def mock_pacth_request(self, name, age):
        url = 'mock_put_request'
        data = {
            'name': name,
            'age': age
        }
        return self._rest_call(url, 'PATCH', data=data)


class ExampleClient(RestClientFactory):

    @classmethod
    def client_class(cls, profile):
        return Example
