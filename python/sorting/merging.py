#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Sorting by merging"""


def merge(src, i, i_end, j, j_end, dst, k):
    x = y = float('inf')
    if i < i_end:
        x = src[i]
    if j < j_end:
        y = src[j]
    while i < i_end and j < j_end:
        if x <= y:
            dst[k] = x
            i += 1
            if i < i_end:
                x = src[i]
        else:
            dst[k] = y
            j += 1
            if j < j_end:
                y = src[j]
        k += 1

    for i in range(i, i_end):
        dst[k] = src[i]
        k += 1

    for j in range(j, j_end):
        dst[k] = src[j]
        k += 1


def merge_sort(A):
    A_id = id(A)
    n = len(A)
    B = [0] * n
    r = 1  # run length
    while r < n:
        # Invariant: subarrays (or runs) A[r*i:r*(i+1)] are sorted
        for i in range(0, n, 2 * r):
            # Merge a pair of adjacent runs
            j = i_end = min(i + r, n)
            j_end = min(j + r, n)
            merge(A, i, i_end, j, j_end, B, i)
        A, B = B, A
        r *= 2

    if id(A) != A_id:
        for i in range(n):
            B[i] = A[i]
