#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

import graph


class APSPTestCase(unittest.TestCase):
    def test_apsp(self):
        n = 10 ** 1
        m = 10 * n
        for _ in range(100):
            G = graph.AdjacencyList.random_graph(n, m, weighted=True)
            A, _ = graph.apsp.by_sssp(G)
            B, _ = graph.apsp.mm(G)
            C, _ = graph.apsp.floyd_warshall(G)
            D, _ = graph.apsp.johnson(G)
            for a, b, c, d in zip(A, B, C, D):
                for x, y, z, w in zip(a, b, c, d):
                    self.assertEqual(x, y)
                    self.assertEqual(y, z)
                    self.assertEqual(z, w)
