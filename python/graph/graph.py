#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


class AdjacencyList:
    def __init__(self, directed=False, weighted=False):
        self.directed = directed
        self.weighted = weighted
        self._edges = {}  # dict of dict
        self._m = 0  # Number of edges
        self._n = 0  # Number of vertices

    def insert(self, u, v, w=1):
        """Insert an edge (u, v) with a weight w"""
        self._n = max(self._n, u + 1, v + 1)
        if not (u, v) in self:
            self._m += 1
        self._add_edge(u, v, w)
        if not self.directed:
            self._add_edge(v, u, w)

    def num_edges(self):
        return self._m

    def num_vertices(self):
        return self._n

    def _add_edge(self, u, v, w):
        self._edges.setdefault(u, {})[v] = w

    def __contains__(self, edge):
        u, v = edge
        return v in self[u]

    def __getitem__(self, u):
        try:
            return self._edges[u]
        except KeyError:
            return {}

    def __iter__(self):
        yield from self._edges

    @classmethod
    def random_graph(cls, n, m, directed=False, weighted=False, max_weight=100):
        G = cls(directed=directed, weighted=weighted)
        for e in cls._gen_edges(n, m, weighted, max_weight):
            G.insert(*e)
        return G

    @classmethod
    def _gen_edges(cls, n, m, weighted, max_weight):
        if not weighted:
            w = 1
        for _ in range(m):
            u = random.randrange(n)
            # v is generated from {0, 1, ..., n - 1} - {u}
            v = random.randrange(u + 1, u + n) % n
            if weighted:
                w = random.randrange(1, max_weight)
            yield (u, v, w)
