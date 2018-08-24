#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def bm(text, pattern, alphabet):
    """Boyer-Moore"""
    n = len(text) - 1
    m = len(pattern)
    table, char2num = make_table(pattern, alphabet)
    indices = []
    i = m - 1
    while i < n:
        j = m - 1
        while j >= 0:
            if text[i] != pattern[j]:
                break
            i -= 1
            j -= 1
        if j < 0:
            indices.append(i + 1)
        i += max(table[char2num[text[i]]], m - j)
    return indices


def make_table(pattern, alphabet):
    m = len(pattern)
    d = len(alphabet)
    char2num = {c: i for (i, c) in enumerate(alphabet)}
    table = [m] * d
    for i in range(m - 1):
        table[char2num[pattern[i]]] = m - 1 - i
    return (table, char2num)
