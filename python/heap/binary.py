#!/usr/bin/env python3
# -*- coding: utf-8 -*-



class BinaryHeap:
    """A binary min heap"""

    def __init__(self, A=None):
        if A is None:
            self.A = []
        else:
            self.A = list(A)
            self._construct()

    def insert(self, k):
        """Insert a key to the heap"""
        self.A.append(k)
        self._siftup(len(self.A) - 1)

    def extract(self):
        """Remove and return the minimum element"""
        ret = self.A.pop()
        if self.A:
            ret, self.A[0] = self.A[0], ret
            self._siftdown(0)
        return ret

    def change_key(self, i, k):
        """Change the ith element to k"""
        old = self.A[i]
        self.A[i] = k
        if old < k:
            # Increase key
            self._siftdown(i)
        elif old > k:
            # Decrease key
            self._siftup(i)

    def _siftup(self, i):
        """Move up A[i] as much as necessary"""
        k = self.A[i]
        while i > 0:
            j = (i - 1) // 2
            if k > self.A[j]:
                break
            self.A[i] = self.A[j]
            i = j
        self.A[i] = k

    def _siftdown(self, i):
        """Move down A[i] as much as necessary"""
        k = self.A[i]
        j = i * 2 + 1
        n = len(self.A)
        while j < n:
            if j + 1 < n and self.A[j] > self.A[j + 1]:
                j = j + 1
            if k < self.A[j]:
                break
            self.A[i] = self.A[j]
            i = j
            j = i * 2 + 1
        self.A[i] = k

    def _construct(self):
        for i in range((len(self.A) // 2) - 1, -1, -1):
            self._siftdown(i)

    def __bool__(self):
        return bool(self.A)

    def __len__(self):
        return len(self.A)
