#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class SSSP:
    def __init__(self, G):
        self.G = G
        self.n = n = G.num_vertices()
        self.dists = [float('inf')] * n
        self.preds = [None] * n

    def clear(self):
        for i in range(self.n):
            self.dists[i] = float('inf')
            self.preds[i] = None

    def relax(self, u, v, w):
        d = self.dists[u] + w
        if d < self.dists[v]:
            self.dists[v] = d
            self.preds[v] = u
            return True
        else:
            return False


def gen_sssp_func(cls):
    def f(G, s):
        c = cls(G)
        c.main(s)
        return (c.dists, c.preds)
    return f
