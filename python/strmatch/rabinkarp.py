#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .common import *


def rabin_karp(text, pattern, alphabet, q=562448657):
    n = len(text)
    m = len(pattern)
    d = len(alphabet)
    char2num = {c: i for (i, c) in enumerate(alphabet)}
    h = (d ** (m - 1)) % q

    p = 0
    t = 0
    for i in range(m):
        p = (d * p + char2num[pattern[i]]) % q
        t = (d * t + char2num[text[i]]) % q

    indices = []
    for s in range(n - m):
        if p == t:
            if is_valid_shift(text, pattern, s):
                indices.append(s)
        if s < n - m - 1:
            t = (d * (t - char2num[text[s]] * h) + char2num[text[s + m]]) % q
    return indices
