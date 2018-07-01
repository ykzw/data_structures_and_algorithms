#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import random


def _benchmark(func, A, ml):
    begin = time.time()
    func(A)
    end = time.time()

    template = '{{:{}}}  {{:.4}} s'.format(ml)
    print(template.format(func.__name__, end - begin))


def benchmark(p, pred=lambda x: x):
    import sorting
    n = int(2 ** p)
    print('===== Sort 2^{} = {} elements =====\n'.format(p, n))
    A = [random.randrange(n * 2) for i in range(n)]
    max_length = max(len(name) for name in sorting.__dict__ if pred(name))
    for name, attr in sorting.__dict__.items():
        if pred(name):
            _benchmark(attr, A[:], max_length)
    print()


def benchmark_all():
    benchmark(9.7, lambda name: 'sort' in name)


def benchmark_fastonly():
    candidates = {'quick', 'heap', 'merge', 'radix', 'python'}
    pred = lambda name: 'sort' in name and any(c in name for c in candidates)
    benchmark(18.3, pred)



if __name__ == "__main__":
    benchmark_fastonly()
