#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
from numpy import uint32


class HopscotchHashTable:
    TOMBSTONE = object()
    H = 32

    def __init__(self):
        self._nelem = 0
        self._nslot = 8
        self._table = [None] * self._nslot
        self._hop_info = [uint32()] * self._nslot

    def insert(self, key):
        def retry():
            self._resize()
            return self.insert(key)

        if self.search(key):
            return False

        s = i = hash(key) % self._nslot

        # Search an empty slot
        while self._table[i] is not None and self._table[i] is not self.TOMBSTONE:
            i += 1
            if i == self._nslot:
                return retry()

        while i - s >= self.H:
            i = self._move_closer(i, s)
            if i == -1:
                return retry()

        if self._table[i] is not None and self._table[i] is not self.TOMBSTONE:
            return retry()

        self._table[i] = key
        self._hop_info[s] |= (1 << (i - s))
        return True

    def search(self, key):
        s = hash(key) % self._nslot
        hop = self._hop_info[s]
        i = 0
        while hop > 0:
            nz = ctz(hop)
            i += nz
            if self._table[s + i] == key:
                return True
            hop >>= nz + 1
        return False

    def delete(self, key):
        s = hash(key) % self._nslot
        hop = self._hop_info[s]
        i = 0
        while hop > 0:
            nz = ctz(hop)
            i += nz
            if self._table[s + i] == key:
                self._table[s + i] = self.TOMBSTONE
                self._hop_info[s] &= ~(1 << i)
                return True
            hop >>= nz + 1
        return False

    def _move_closer(self, i, h):
        for j in range(i - (self.H - 1), i):
            hop = self._hop_info[j]
            for k in range(i - j):
                if (hop & (1 << k)) == 1:
                    # Swap keys
                    self._table[i], self._table[j + k] = self._table[j + k], self._table[i]
                    self._hop_info[j] &= ~(1 << k)
                    self._hop_info[j] |= 1 << (i - j)
                    i = j + k
                    return i
        return -1

    def _resize(self):
        oldtable = self._table
        self._nslot *= 2
        self._table = [None] * self._nslot
        self._hop_info = [uint32()] * self._nslot
        for key in oldtable:
            if key is None or key is self.TOMBSTONE:
                continue
            self.insert(key)


def ctz(x):
    y = isolate_rightmost_one(x)
    bz = 0 if y else 1
    b4 = 0 if (y & 0x0000ffff) else 16
    b3 = 0 if (y & 0x00ff00ff) else 8
    b2 = 0 if (y & 0x0f0f0f0f) else 4
    b1 = 0 if (y & 0x33333333) else 2
    b0 = 0 if (y & 0x55555555) else 1
    return bz + b4 + b3 + b2 + b1 + b0;


def isolate_rightmost_one(x):
    return x & -x
