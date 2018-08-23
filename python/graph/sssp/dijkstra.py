#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from heap import BinaryHeap as PriorityQueue
from .common import *


class Dijkstra(SSSP):
    def main(self, s):
        self.dists[s] = 0

        pq = PriorityQueue()
        for u in range(self.n):
            pq.insert(float('inf'), u)

        pq.decrease_key(s, 0)
        while pq:
            _, u = pq.extract()
            for v in self.G[u]:
                if self.relax(u, v, self.G[u][v]):
                    pq.decrease_key(v, self.dists[v])


dijkstra = gen_sssp_func(Dijkstra)
