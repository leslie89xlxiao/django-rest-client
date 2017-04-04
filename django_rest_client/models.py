from jsonfield import JSONField

from django.db import models


class DjangoRestClient(models.Model):
    name = models.CharField(max_length=32, primary_key=True)
    config = JSONField(default={})

    class Meta:
        db_table = 'django_rest_client'
