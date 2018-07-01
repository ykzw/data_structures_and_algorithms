#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Sorting by insertion"""


def insertion_sort(A):
    for i in range(1, len(A)):
        # Invariant: A[:i] is sorted
        a = A[i]
        # "Insert" A[i] into an appropriate position within A[:i+1]
        j = i - 1
        while j >= 0 and a < A[j]:
            # Shift elements larger than A[i] to the right
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = a
