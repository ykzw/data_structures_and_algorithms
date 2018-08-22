#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import collections


def bfs(G, s):
    n = G.num_vertices()
    dists = [float('inf')] * n
    preds = [None] * n

    dists[s] = 0
    queue = collections.deque([s])
    while queue:
        u = queue.popleft()
        for v in G[u]:
            if dists[u] + 1 < dists[v]:
                dists[v] = dists[u] + 1
                preds[v] = u
                queue.append(v)

    return (dists, preds)
