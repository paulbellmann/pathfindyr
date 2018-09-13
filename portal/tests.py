# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from pathfinding import dijkstra, grab_data

# Create your tests here.
class AlgorithmTest(TestCase):
    """Grabs data from XML and test if the algorithm will
    return the shortest path from start to end
    """

    def test_shortest_path(self):
        self.graph, self.graphgraph_helper = grab_data('nodes.xml')
        right_path = dijkstra(self.graph, 1, 13)
        wrong_path = dijkstra(self.graph, 1, 877)

        self.assertEqual(right_path, [1, 3, 12, 13])
        self.assertEqual(wrong_path, 'Path not reachable')
