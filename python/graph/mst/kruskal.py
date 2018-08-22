#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from disjointset import DisjointPythonSets as DisjointSets


def kruskal(G):
    ds = DisjointSets()
    weight_edge_list = []
    for u in G:
        ds.make_set(u)
        for v in G[u]:
            weight_edge_list.append((G[u][v], u, v))

    mst = set()
    weight_edge_list.sort()
    for w, u, v in weight_edge_list:
        if ds.find_set(u) != ds.find_set(v):
            mst.add((u, v))
            ds.union(u, v)
    return mst
