#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .bm import make_table


def horspool(text, pattern, alphabet):
    n = len(text) - 1
    m = len(pattern)
    table, char2num = make_table(pattern, alphabet)
    indices = []
    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0:
            if text[i + j] != pattern[j]:
                break
            j -= 1
        if j < 0:
            indices.append(i)
        i += table[char2num[text[i + m - 1]]]
    return indices
