#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

from heap import SkewHeap as PriorityQueue


def prim(G):
    n = G.num_vertices()
    parents = [-1] * n

    pq = PriorityQueue()
    for u in G:
        pq.insert(float('inf'), u)

    pq.decrease_key(u, 0)
    while pq:
        _, u = pq.extract()
        for v in G[u]:
            if v in pq and G[u][v] < pq[v]:
                parents[v] = u
                pq.decrease_key(v, G[u][v])

    mst = set()
    for u, v in enumerate(parents):
        if v >= 0:
            mst.add((u, v))
    return mst
