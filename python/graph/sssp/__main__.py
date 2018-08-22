#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import random

from graph import AdjacencyList as Graph
from bellmanford import *
from dag import *
from dijkstra import *


def benchmark():
    n = 10 ** 4
    m = 10 * n
    G = Graph.random_DAG(n, m, weighted=True)

    s = random.randrange(n)

    def h(func, name):
        begin = time.time()
        dists, _ = func(G, s)
        end = time.time()
        print('* {:<12}  {:.4} s'.format(name, end - begin))
        print('-- sum of distances:',
              sum(d for d in dists if d < float('inf')))
        print()

    h(bellman_ford, 'Bellman-Ford')
    h(dag, 'DAG')
    h(dijkstra, 'Dijkstra')


if __name__ == '__main__':
    benchmark()
