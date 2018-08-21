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


def _benchmark(heap_type, keys):
    h = None

    def construct():
        nonlocal h
        h = heap_type(keys)

    def extract():
        for _ in keys:
            h.extract()

    def insert():
        for k in keys:
            h.insert(k)

    def change_key():
        for i in range(len(keys)):
            h.change_key(i, -i)

    print(heap_type.__name__)
    t = measure(construct)
    print('* Construct   {:.3} s'.format(t))
    t = measure(extract)
    print('* Extract     {:.3} s'.format(t))
    t = measure(insert)
    print('* Insert      {:.3} s'.format(t))
    t = measure(change_key)
    print('* Change key  {:.3} s'.format(t))
    print()


def benchmark():
    n = 10 ** 5
    keys = list(range(n))
    random.shuffle(keys)

    print('=====', n, 'keys =====\n')

    _benchmark(BinaryHeap, keys)


if __name__ == "__main__":
    benchmark()
