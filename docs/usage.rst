=====
Usage
=====

To use django-highcharts-models in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_highcharts_models.apps.DjangoHighchartsModelsConfig',
        ...
    )

Add django-highcharts-models's URL patterns:

.. code-block:: python

    from django_highcharts_models import urls as django_highcharts_models_urls


    urlpatterns = [
        ...
        url(r'^', include(django_highcharts_models_urls)),
        ...
    ]
