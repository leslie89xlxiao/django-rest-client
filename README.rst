Django Rest Client
==================

Rest Client aimed to be a python utility kit for all rest services of Ctrip Platform.
Currently it has covered clients for all tars/case-related rest services.

Requirements
------------

* **Python**: 2.7, 3.3, 3.4, 3.5
* **Django**: 1.8, 1.10, 1.11
* **DRF**: 3.6

Installation
------------

Install using pip:

.. code-block:: sh

    pip install django-rest-client

Then add ``'django_rest_client'`` to your ``INSTALLED_APPS``.

.. code-block:: python

    INSTALLED_APPS = [
        ...
        'django_rest_client',
    ]
