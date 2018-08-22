#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def dfs(G):
    n = G.num_vertices()
    visited = [False] * n

    vertices = []
    def visit(u):
        visited[u] = True
        for v in G[u]:
            if visited[v]:
                continue
            visit(v)
        vertices.append(u)

    for u in G:
        if visited[u]:
            continue
        visit(u)

    vertices.reverse()
    return vertices

topological_sort = dfs
