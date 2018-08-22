#!/usr/bin/env python3
# -*- coding: utf-8 -*-



class BinaryHeap:
    """A binary min heap"""

    def __init__(self, A=None):
        self.id2pos = {}
        if A is None:
            self.A = []
        else:
            # Each element of A is a pair of a key and identity
            self.A = list(A)
            self._construct()

    def merge(self, other):
        """Merge the "other" heap into self"""
        # Concatanate the other array and call _construct
        self.A.extend(other.A)
        self._construct()

    def insert(self, key, id_):
        """Insert an item to the heap"""
        self.A.append((key, id_))
        self._siftup(len(self.A) - 1)

    def extract(self):
        """Remove and return the item with the minimum key"""
        ret = self.A.pop()
        if self.A:
            self.id2pos[ret[1]] = 0
            ret, self.A[0] = self.A[0], ret
            self._siftdown(0)
        self.id2pos.pop(ret[1])
        return ret

    def decrease_key(self, id_, newkey):
        """Decrease the key of id_ to k"""
        pos = self.id2pos[id_]
        self.A[pos] = (newkey, id_)
        self._siftup(pos)

    def _siftup(self, i):
        """Move up A[i] as much as necessary"""
        item = self.A[i]
        while i > 0:
            parent = (i - 1) // 2
            if item > self.A[parent]:
                break
            self._set_item(i, self.A[parent])
            i = parent
        self._set_item(i, item)

    def _siftdown(self, i):
        """Move down A[i] as much as necessary"""
        item = self.A[i]
        child = i * 2 + 1
        n = len(self.A)
        while child < n:
            if child + 1 < n and self.A[child] > self.A[child + 1]:
                child = child + 1
            if item < self.A[child]:
                break
            self._set_item(i, self.A[child])
            i = child
            child = i * 2 + 1
        self._set_item(i, item)

    def _construct(self):
        for i, (_, id_) in enumerate(self.A):
            self.id2pos[id_] = i
        for i in range((len(self.A) // 2) - 1, -1, -1):
            self._siftdown(i)

    def _set_item(self, pos, item):
        self.id2pos[item[1]] = pos
        self.A[pos] = item

    def __getitem__(self, id_):
        return self.A[self.id2pos[id_]][0]

    def __contains__(self, id_):
        return id_ in self.id2pos

    def __bool__(self):
        return bool(self.A)

    def __len__(self):
        return len(self.A)
