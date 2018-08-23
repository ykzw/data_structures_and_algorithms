#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from searchtree import *


def _benchmark(tree_type, keys):
    import time
    t = tree_type()
    begin = time.time()
    for k in keys:
        t.insert(k)
    end = time.time()

    print(tree_type.__name__)
    print('* Insert in {:.3} s'.format(end - begin))
    print('* Height is {}'.format(t.height()))

    begin = time.time()
    for k in keys:
        t.search(k)
    end = time.time()
    print('* Search in {:.3} s'.format(end - begin))

    begin = time.time()
    for k in keys:
        t.delete(k)
    end = time.time()
    print('* Delete in {:.3} s'.format(end - begin))

    print()


def benchmark():
    import random
    n = 10 ** 5
    keys = list(range(n))
    random.shuffle(keys)

    print('=====', n, 'keys =====\n')

    _benchmark(BinarySearchTree, keys)
    _benchmark(RedBlackTree, keys)
    _benchmark(BTree, keys)


if __name__ == "__main__":
    benchmark()
