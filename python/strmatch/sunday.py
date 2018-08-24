#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .common import is_valid_shift


def sunday(text, pattern, alphabet):
    n = len(text)
    m = len(pattern)
    table, char2num = make_table(pattern, alphabet)

    indices = []
    i = 0
    try:
        while i <= n - m:
            if is_valid_shift(text, pattern, i):
                indices.append(i)
            i += table[char2num[text[i + m]]]
    except IndexError:
        pass
    return indices


def make_table(pattern, alphabet):
    m = len(pattern)
    d = len(alphabet)
    char2num = {c: i for (i, c) in enumerate(alphabet)}
    table = [m + 1] * d
    for i in range(m):
        table[char2num[pattern[i]]] = m - i
    return (table, char2num)
