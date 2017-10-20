=============================
django-highcharts-models
=============================

.. image:: https://badge.fury.io/py/django-highcharts-models.svg
    :target: https://badge.fury.io/py/django-highcharts-models

.. image:: https://travis-ci.org/darwing1210/django-highcharts-models.svg?branch=master
    :target: https://travis-ci.org/darwing1210/django-highcharts-models

.. image:: https://codecov.io/gh/darwing1210/django-highcharts-models/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/darwing1210/django-highcharts-models

Django highcharts models to create charts

Documentation
-------------

The full documentation is at https://django-highcharts-models.readthedocs.io.

Quickstart
----------

Install django-highcharts-models::

    pip install django-highcharts-models

Add it to your `INSTALLED_APPS`:

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

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
