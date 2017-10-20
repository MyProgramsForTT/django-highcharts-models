# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(
        regex="^Chart/~create/$",
        view=views.ChartCreateView.as_view(),
        name='Chart_create',
    ),
    url(
        regex="^Chart/(?P<pk>\d+)/~delete/$",
        view=views.ChartDeleteView.as_view(),
        name='Chart_delete',
    ),
    url(
        regex="^Chart/(?P<pk>\d+)/$",
        view=views.ChartDetailView.as_view(),
        name='Chart_detail',
    ),
    url(
        regex="^Chart/(?P<pk>\d+)/~update/$",
        view=views.ChartUpdateView.as_view(),
        name='Chart_update',
    ),
    url(
        regex="^Chart/$",
        view=views.ChartListView.as_view(),
        name='Chart_list',
    ),
	url(
        regex="^ChartSerie/~create/$",
        view=views.ChartSerieCreateView.as_view(),
        name='ChartSerie_create',
    ),
    url(
        regex="^ChartSerie/(?P<pk>\d+)/~delete/$",
        view=views.ChartSerieDeleteView.as_view(),
        name='ChartSerie_delete',
    ),
    url(
        regex="^ChartSerie/(?P<pk>\d+)/$",
        view=views.ChartSerieDetailView.as_view(),
        name='ChartSerie_detail',
    ),
    url(
        regex="^ChartSerie/(?P<pk>\d+)/~update/$",
        view=views.ChartSerieUpdateView.as_view(),
        name='ChartSerie_update',
    ),
    url(
        regex="^ChartSerie/$",
        view=views.ChartSerieListView.as_view(),
        name='ChartSerie_list',
    ),
	]
