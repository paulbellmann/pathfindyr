# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from algo import dijkstra, grab_data

# Create your views here.


def index(request):
    graph, graph_helper = grab_data('knoten2.xml')

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

    print graph_backup

    new_test = []

    for each in path:
        print graph_backup[each]
        new_test.append(graph_backup[each])

    print "####"
    print new_test
    print "####"

    # only keep nodes needed for the route
    needed_nodes = { each: graph_backup[each] for each in path }

    context = {'graph': new_test, 'mode': 'route', 'path': path}
    return render(request, 'home.html', context)