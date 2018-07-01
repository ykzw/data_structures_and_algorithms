#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Sorting by exchanging"""


def bubble_sort(A):
    n = len(A)
    for i in range(n):
        for j in range(n - 1):
            if A[j] > A[j + 1]:
                # "Bubble" up if not sorted
                A[j], A[j + 1] = A[j + 1], A[j]


def bubble_sort_opt(A):
    # Slightly optimized version
    n = len(A)
    while n > 0:
        m = 0
        for i in range(n - 1):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                # Save the maximum index where a swap occurs
                m = i + 1
        n = m


def hoare_partition(A, lo, hi):
    pivot = A[lo]
    i = lo - 1
    j = hi + 1
    while i < j:
        # Invariant: A[lo:i+1] <= pivot and A[j-1:hi] >= pivot
        i += 1
        while i <= j and A[i] < pivot:
            i += 1
        j -= 1
        while i <= j and A[j] > pivot:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
    return j


def hoare_quicksort(A):
    def rec(lo, hi):
        if lo < hi:
            p = hoare_partition(A, lo, hi)
            rec(lo, p)
            rec(p + 1, hi)

    rec(0, len(A) - 1)


def lomuto_partition(A, lo, hi):
    pivot = A[hi]
    i = lo - 1
    for j in range(lo, hi):
        # Invariant: A[lo:i+1] <= pivot and A[i+1:j] > pivot
        if A[j] < pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[hi] = A[hi], A[i + 1]
    return i + 1


def lomuto_quicksort(A):
    def rec(lo, hi):
        if lo < hi:
            p = lomuto_partition(A, lo, hi)
            rec(lo, p - 1)
            rec(p + 1, hi)

    rec(0, len(A) - 1)
