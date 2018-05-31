#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Sorting algorithms'''

import time
import types
import heapq
import random
import bisect


def python_sort(A):
    A.sort()


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


def selection_sort(A):
    n = len(A)
    for i in range(n):
        # Invariant: A[:i] is sorted
        # "Select" the smallest element among A[i:]
        _, j = min((A[j], j) for j in range(i, n))
        # And swap A[i] and A[j]
        A[i], A[j] = A[j], A[i]


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



def _benchmark(func, A, ml):
    begin = time.time()
    func(A)
    end = time.time()

    template = '{{:{}}}  {{:.4}} s'.format(ml)
    print(template.format(func.__name__, end - begin))


def benchmark(p, pred=lambda x: x):
    import sort
    n = int(2 ** p)
    print('===== Sort 2^{} = {} elements =====\n'.format(p, n))
    A = [random.randrange(n * 2) for i in range(n)]
    max_length = max(len(name) for name in sort.__dict__ if pred(name))
    for name, attr in sort.__dict__.items():
        if pred(name):
            _benchmark(attr, A[:], max_length)
    print()


def benchmark_all():
    benchmark(9.7, lambda name: 'sort' in name)


def benchmark_fastonly():
    candidates = {'quick', 'heap', 'merge', 'radix', 'python'}
    pred = lambda name: 'sort' in name and any(c in name for c in candidates)
    benchmark(18.3, pred)



if __name__ == "__main__":
    benchmark_fastonly()
