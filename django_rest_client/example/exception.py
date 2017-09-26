from django_rest_client.exceptions import ServerResponseError


class ExampleClientError(ServerResponseError):
    pass
