#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from disjointset import *

import time
import random


def _benchmark(disjointset_type, keys):
    n = len(keys)
    ds = disjointset_type()

    print(disjointset_type.__name__)
    begin = time.time()
    for k in keys:
        ds.make_set(k)
    end = time.time()
    print('* Make set  {:.3} s'.format(end - begin))

    t1, t2 = 0.0, 0.0
    current_sets = [{i} for i in range(n)]
    for i in range(5):
        # Union
        for _ in range(n // 10):
            s1, s2 = pop_two_sets(current_sets)
            current_sets.append(s1 | s2)
            m1 = take_one_elem(s1)
            m2 = take_one_elem(s2)
            begin = time.time()
            ds.union(m1, m2)
            end = time.time()
            t1 += end - begin
        # Find set
        begin = time.time()
        for k in keys:
            ds.find_set(k)
        end = time.time()
        t2 += end - begin

    print('* Union     {:.3} s'.format(t1))
    print('* Find set  {:.3} s'.format(t2))
    print()


def benchmark():
    n = 10 ** 4
    keys = list(range(n))
    random.shuffle(keys)

    print('=====', n, 'keys =====\n')

    _benchmark(LinkedListDisjointSets, keys)
    _benchmark(DisjointSetForest, keys)
    _benchmark(DisjointPythonSets, keys)


if __name__ == "__main__":
    benchmark()
