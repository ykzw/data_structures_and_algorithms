#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import unittest

import graph


class SSSPTestCase(unittest.TestCase):
    def test_sssp(self):
        n = 10 ** 2
        m = 10 * n
        for _ in range(100):
            G = graph.AdjacencyList.random_DAG(n, m, weighted=True)
            s = random.randrange(n)
            A, _ = graph.sssp.bellman_ford(G, s)
            B, _ = graph.sssp.dag(G, s)
            C, _ = graph.sssp.dijkstra(G, s)
            for a, b, c in zip(A, B, C):
                self.assertEqual(a, b)
                self.assertEqual(b, c)
