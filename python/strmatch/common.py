#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import string
import itertools


def is_valid_shift(text, pattern, s):
    m = len(pattern)
    shifted_txt = itertools.islice(text, s, s + m)

    return all(tsi == pi for tsi, pi in
               itertools.zip_longest(shifted_txt, pattern, fillvalue=''))


def random_string(alphabet, n):
    return ''.join(random.choices(alphabet, k=n))
