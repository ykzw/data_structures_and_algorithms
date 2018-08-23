#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

import graph
import disjointset


class MSTTestCase(unittest.TestCase):
    def test_mst(self):
        n = 10 ** 2
        m = 10 * n
        for _ in range(100):
            G = graph.AdjacencyList.random_graph(n, m, weighted=True)
            A = graph.mst.kruskal(G)
            self.check_treeness(G, A)
            B = graph.mst.prim(G)
            self.check_treeness(G, B)
            wa = sum(G[u][v] for u, v in A)
            wb = sum(G[u][v] for u, v in B)
            self.assertEqual(wa, wb)

    def check_treeness(self, G, edges):
        ds = disjointset.DisjointPythonSets()
        for u in G:
            ds.make_set(u)
        for u, v in edges:
            self.assertTrue(ds.union(u, v))
