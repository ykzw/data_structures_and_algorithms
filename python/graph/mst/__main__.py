#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

from graph import AdjacencyList as Graph
from kruskal import kruskal
from prim import prim


def benchmark():
    n = 10 ** 4
    m = 10 * n
    G = Graph.random_graph(n, m, weighted=True)

    begin = time.time()
    A = kruskal(G)
    end = time.time()
    print('Kruskal: {:.5} s'.format(end - begin))
    print('-- total weight:', sum(G[u][v] for u, v in A))
    print()

    begin = time.time()
    B = prim(G)
    end = time.time()
    print('   Prim: {:.5} s'.format(end - begin))
    print('-- total weight:', sum(G[u][v] for u, v in B))


if __name__ == '__main__':
    benchmark()
