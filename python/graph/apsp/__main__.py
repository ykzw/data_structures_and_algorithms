#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import random

from graph import AdjacencyList as Graph
from graph.apsp import *


def benchmark():
    n = 10 ** 2
    m = 10 * n
    G = Graph.random_graph(n, m, weighted=True)

    def h(func, name):
        begin = time.time()
        dists, _ = func(G)
        end = time.time()
        print('* {:<14}  {:.4} s'.format(name, end - begin))
        print('-- sum of distances:',
              sum(sum(d for d in ds if d < float('inf'))
                  for ds in dists))
        print()

    h(by_sssp, 'By SSSP')
    h(mm, 'MM')
    h(floyd_warshall, 'Floyd-Warshall')
    h(johnson, 'Johnson')


if __name__ == '__main__':
    benchmark()
