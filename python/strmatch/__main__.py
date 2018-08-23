#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import random
import string

from strmatch import *


def _benchmark(func, name, text, pattern):
    begin = time.time()
    print(func(text, pattern))
    end = time.time()
    print('* {:<12}  {:.3} s'.format(name, end - begin))


def benchmark():
    n = 10 ** 5
    m = 8
    alphabet = 'atcg'
    text = ''.join(random.choice(alphabet) for _ in range(n))
    pattern = ''.join(random.choice(alphabet) for _ in range(m))

    _benchmark(python, 'Python index', text, pattern)
    def wrapper(func):
        def f(text, pattern):
            return func(text, pattern, alphabet)
        return f
    _benchmark(wrapper(rabin_karp), 'Rabin-Karp', text, pattern)
    _benchmark(wrapper(automaton), 'Automaton', text, pattern)
    _benchmark(kmp, 'KMP', text, pattern)

    print()


if __name__ == "__main__":
    benchmark()
