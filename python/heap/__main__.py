#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from heap import *

import time
import random


def measure(func):
    begin = time.time()
    func()
    end = time.time()
    return end - begin


def _benchmark(heap_type, items):
    h = None

    def construct():
        nonlocal h
        h = heap_type(items)

    def extract():
        for _ in items:
            h.extract()

    def insert():
        for k, id_ in items:
            h.insert(k, id_)

    def decrease_key():
        for i in range(len(items)):
            h.decrease_key(i, i - 100)

    n = len(items)
    h2 = heap_type((k + n, id_ + n) for k, id_ in items)
    def merge():
        h.merge(h2)

    print(heap_type.__name__)
    t = measure(construct)
    print('* Construct     {:.3} s'.format(t))
    t = measure(extract)
    print('* Extract       {:.3} s'.format(t))
    t = measure(insert)
    print('* Insert        {:.3} s'.format(t))
    t = measure(decrease_key)
    print('* Decrease key  {:.3} s'.format(t))
    t = measure(merge)
    print('* Merge         {:.3} s'.format(t))
    print()


def benchmark():
    n = 10 ** 5
    keys = list(range(n))
    items = [(k, k) for k in keys]
    random.shuffle(items)

    print('=====', n, 'items =====\n')

    _benchmark(BinaryHeap, items)
    _benchmark(BinomialHeap, items)
    _benchmark(PairingHeap, items)
    _benchmark(SkewHeap, items)
    _benchmark(FibonacciHeap, items)


if __name__ == "__main__":
    benchmark()
