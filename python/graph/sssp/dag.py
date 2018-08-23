#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from graph.search import topological_sort
from .common import *


class DAG(SSSP):
    def main(self, s):
        self.dists[s] = 0

        topo = topological_sort(self.G)
        for u in topo:
            for v in self.G[u]:
                self.relax(u, v, self.G[u][v])


dag = gen_sssp_func(DAG)
