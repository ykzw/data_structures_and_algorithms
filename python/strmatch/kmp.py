#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def kmp(text, pattern):
    """Knuth-Morris-Pratt"""
    m = len(pattern)
    p = compute_prefix(pattern)
    q = 0
    indices = []
    for i, ti in enumerate(text):
        q = match_with_prefix(pattern, p, q, ti)
        if q == m:
            indices.append(i - m + 1)
            q = p[q - 1]
    return indices


def compute_prefix(pattern):
    m = len(pattern)
    p = [0] * m
    k = 0
    for q in range(1, m):
        p[q] = k = match_with_prefix(pattern, p, k, pattern[q])
    return p


def match_with_prefix(pattern, p, q, a):
    while q > 0 and pattern[q] != a:
        q = p[q - 1]
    if pattern[q] == a:
        q += 1
    return q
