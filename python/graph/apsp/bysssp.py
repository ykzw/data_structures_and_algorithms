#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .common import *
from graph.sssp import dijkstra


class BySSSP(APSP):
    def main(self):
        for u in range(self.n):
            dists, _ = dijkstra(self.G, u)
            self.dists[u] = dists[:]


by_sssp = gen_apsp_func(BySSSP)
