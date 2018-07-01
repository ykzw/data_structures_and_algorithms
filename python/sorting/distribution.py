#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Sorting by distribution"""


def radix_sort(A):
    n = len(A)
    B = [0] * n
    nbits = 8
    base = 2 ** nbits
    mask = (1 << nbits) - 1
    max_bits = max(len(bin(a)) for a in A) - 2
    for i in range(0, max_bits, nbits):
        # Invariant: A is sorted according to lower (i / nbits) digits of base 2^nbits
        counts = [0] * base
        # Compute the sizes of buckets
        for a in A:
            d = (a >> i) & mask
            counts[d] += 1
        # Prefix sum
        s = 0
        for j in range(base):
            t = counts[j]
            counts[j] = s
            s += t
        # Scatter
        for a in A:
            d = (a >> i) & mask
            j = counts[d]
            B[j] = a
            counts[d] += 1
        A, B = B, A

    if ((max_bits // nbits) & 1) == 0:
        # If the number of passes is odd, B holds the final result, so move it to A
        for i in range(n):
            B[i] = A[i]
