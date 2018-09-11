# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from algo import dijkstra, grab_data

# Create your views here.


def index(request):
    # grab data from xml
    graph, graph_helper = grab_data('knoten2.xml')

    # make a list from all the points
    data = []
    for each, val in graph_helper.items():
        data.append(val)

    context = {'graph': data, 'mode': 'all'}
    return render(request, 'home.html', context)


def route(request):
    # grab data from xml
    graph, graph_helper = grab_data('knoten2.xml')
    graph_backup = graph_helper.copy()

    # get shortest path
    start, end = int(request.GET['start']), int(request.GET['end'])
    path = dijkstra(graph, start, end)

    # only keep nodes needed for the route
    data = []
    for each in path:
        data.append(graph_backup[each])

    context = {'graph': data, 'mode': 'route', 'path': path}
    return render(request, 'home.html', context)