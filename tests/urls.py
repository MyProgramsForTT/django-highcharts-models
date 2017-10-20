# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from django_highcharts_models.urls import urlpatterns as django_highcharts_models_urls

urlpatterns = [
    url(r'^', include(django_highcharts_models_urls, namespace='django_highcharts_models')),
]
