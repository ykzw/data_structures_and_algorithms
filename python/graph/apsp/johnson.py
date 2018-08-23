#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .common import *
from graph.sssp import bellman_ford, dijkstra


class Johnson(APSP):
    class graph_wrapper:
        def __init__(self, G):
            self.G = G
            n = G.num_vertices()
            self.h = [0] * n
            self._cache = {}
            self._cache[n] = {i: 0 for i in range(n)}

        def num_vertices(self):
            return self.G.num_vertices() + 1

        def set_h(self, dists):
            self.h = dists[:]

        def correct_dists(self, u, dists):
            return [d + self.h[v] - self.h[u] for v, d in enumerate(dists)]

        def __iter__(self):
            yield from self.G
            yield self.G.num_vertices()

        def __getitem__(self, u):
            if u not in self._cache:
                self._cache[u] = {v: self.G[u][v] + self.h[u] - self.h[v]
                                  for v in self.G[u]}
            return self._cache[u]

    def main(self):
        Gprime = self.graph_wrapper(self.G)
        dists, _ = bellman_ford(Gprime, self.n)

        Gprime.set_h(dists)
        for u in range(self.n):
            dists, _ = dijkstra(Gprime, u)
            self.dists[u] = Gprime.correct_dists(u, dists)


johnson = gen_apsp_func(Johnson)
