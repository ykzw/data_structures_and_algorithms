#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def automaton(text, pattern, alphabet):
    m = len(pattern)
    matrix, char2num = transition_matrix(pattern, alphabet)
    indices = []
    q = 0
    for i, ti in enumerate(text):
        q = matrix[q][char2num[ti]]
        if q == m:
            indices.append(i - m + 1)
    return indices


def transition_matrix(pattern, alphabet):
    m = len(pattern)
    d = len(alphabet)
    char2num = {c: i for (i, c) in enumerate(alphabet)}
    matrix = [[0] * d for _ in range(m + 1)]
    for q in range(m + 1):
        for a in alphabet:
            k = min(m + 1, q + 2) - 1
            while not pk_is_suffix_of_pqa(pattern, k, q, a):
                k -= 1
            matrix[q][char2num[a]] = k
    return (matrix, char2num)


def pk_is_suffix_of_pqa(pattern, k, q, a):
    """Judge whether pk (= pattern[:k]) is a suffix of pq + a or not"""
    if k == 0:
        return True

    if k > q + 1 or pattern[k - 1] != a:
        return False

    return all(pattern[k - 2 - i] == pattern[q - 1 - i] for i in range(k - 1))
