#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class CuckooHashTable:
    TOMBSTONE = object()

    def __init__(self):
        self._nelem = 0
        self._nslot = 4
        self._table1 = [None] * self._nslot
        self._table2 = [None] * self._nslot

    def insert(self, key):
        if self.search(key):
            return False

        for _ in range(10):
            s1 = self._hash1(key)
            if self._table1[s1] is None or self._table1[s1] is self.TOMBSTONE:
                self._table1[s1] = key
                self._nelem += 1
                return True
            key, self._table1[s1] = self._table1[s1], key

            s2 = self._hash2(key)
            if self._table2[s2] is None or self._table2[s2] is self.TOMBSTONE:
                self._table2[s2] = key
                self._nelem += 1
                return True
            key, self._table2[s2] = self._table2[s2], key

        self._resize()
        return self.insert(key)

    def search(self, key):
        s1 = self._hash1(key)
        if self._table1[s1] == key:
            return True
        s2 = self._hash2(key)
        if self._table2[s2] == key:
            return True
        return False

    def delete(self, key):
        s1 = self._hash1(key)
        if self._table1[s1] == key:
            self._table1[s1] = self.TOMBSTONE
            self._nelem -= 1
            return True
        s2 = self._hash2(key)
        if self._table2[s2] == key:
            self._table2[s2] = self.TOMBSTONE
            self._nelem -= 1
            return True
        return False

    def _resize(self):
        oldtables = (self._table1, self._table2)
        self._nslot *= 2
        self._table1 = [None] * self._nslot
        self._table2 = [None] * self._nslot
        for table in oldtables:
            for key in table:
                if key is None or key is self.TOMBSTONE:
                    continue
                self.insert(key)

    def _hash1(self, x):
        return hash(x) % self._nslot

    def _hash2(self, x):
        x ^= x >> 16
        x *= 0x85ebca6b
        x ^= x >> 13
        x *= 0xc2b2ae35
        x ^= x >> 16
        return x % self._nslot
