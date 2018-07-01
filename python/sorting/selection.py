#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Sorting by selection"""

import heapq


def selection_sort(A):
    n = len(A)
    for i in range(n):
        # Invariant: A[:i] is sorted
        # "Select" the smallest element among A[i:]
        _, j = min((A[j], j) for j in range(i, n))
        # And swap A[i] and A[j]
        A[i], A[j] = A[j], A[i]


def _siftdown_max(heap, i, end):
    x = heap[i]
    child = 2 * i + 1
    while child < end:
        right = child + 1
        if right < end and not heap[right] < heap[child]:
            child = right
        if x > heap[child]:
            break
        heap[i] = heap[child]
        i = child
        child = 2 * i + 1
    heap[i] = x


def heapsort(A):
    n = len(A)
    heapq._heapify_max(A)
    for i in range(n - 1, 0, -1):
        # Invariants:
        # - A[:i+1] is a max-heap
        # - A[i+1:] is sorted
        # - Elements in A[:i+1] are less than or equal to those in A[i+1:]
        A[0], A[i] = A[i], A[0]
        _siftdown_max(A, 0, i)
