# -*- coding: utf-8 -*-
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)

from .models import (
	Chart,
	ChartSerie,
)


class ChartCreateView(CreateView):

    model = Chart


class ChartDeleteView(DeleteView):

    model = Chart


class ChartDetailView(DetailView):

    model = Chart


class ChartUpdateView(UpdateView):

    model = Chart


class ChartListView(ListView):

    model = Chart


class ChartSerieCreateView(CreateView):

    model = ChartSerie


class ChartSerieDeleteView(DeleteView):

    model = ChartSerie


class ChartSerieDetailView(DetailView):

    model = ChartSerie


class ChartSerieUpdateView(UpdateView):

    model = ChartSerie


class ChartSerieListView(ListView):

    model = ChartSerie

