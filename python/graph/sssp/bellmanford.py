#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .common import *


class BellmanFord(SSSP):
    def main(self, s):
        self.dists[s] = 0
        edge_list = [(u, v, self.G[u][v])
                     for u in self.G for v in self.G[u]]

        for i in range(self.n - 1):
            updated = False
            for u, v, w in edge_list:
                updated |= self.relax(u, v, w)
            if not updated:
                break

        for u, v, w in edge_list:
            if self.dists[v] > self.dists[u] + w:
                raise ValueError('A negative cycle exists!')


bellman_ford = gen_sssp_func(BellmanFord)
