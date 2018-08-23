#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class APSP:
    def __init__(self, G):
        self.G = G
        self.n = n = G.num_vertices()
        self.dists = [[float('inf')] * n for _ in range(n)]
        self.preds = [[None] * n for _ in range(n)]

    def init_dists(self):
        for u in self.G:
            self.dists[u][u] = 0
            for v in self.G[u]:
                self.dists[u][v] = self.G[u][v]


def gen_apsp_func(cls):
    def f(G):
        c = cls(G)
        c.main()
        return (c.dists, c.preds)
    return f
