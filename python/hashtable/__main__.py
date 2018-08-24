#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import random

from hashtable import *


def _benchmark(ht_type, keys):
    def measure(func):
        begin = time.time()
        for k in keys:
            func(k)
        end = time.time()
        return end - begin

    ht = ht_type()
    print(ht_type.__name__)
    print('* Insert  {:.3} s'.format(measure(ht.insert)))
    print('* Search  {:.3} s'.format(measure(ht.search)))
    print('* Delete  {:.3} s'.format(measure(ht.delete)))
    print()


def benchmark():
    n = 10 ** 5
    keys = list(range(n))
    random.shuffle(keys)

    _benchmark(ClosedHashTable, keys)
    _benchmark(LinearHashTable, keys)
    _benchmark(CuckooHashTable, keys)
    _benchmark(HopscotchHashTable, keys)
    _benchmark(PythonHashTable, keys)


if __name__ == '__main__':
    benchmark()
