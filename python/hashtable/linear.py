#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class LinearHashTable:
    TOMBSTONE = object()

    def __init__(self):
        self._nelem = 0
        self._nslot = 8
        self._table = [None] * self._nslot

    def insert(self, key):
        s = self._find_slot(key)
        if self._table[s] != key:
            self._table[s] = key
            self._nelem += 1
            if self._load_factor() > 0.5:
                self._resize()
            return True
        else:
            return False

    def search(self, key):
        s = self._find_slot(key)
        return self._table[s] == key

    def delete(self, key):
        s = self._find_slot(key)
        if self._table[s] == key:
            self._table[s] = self.TOMBSTONE
            self._nelem -= 1
            return True
        else:
            return False

    def _find_slot(self, key):
        i = hash(key) % self._nslot
        while True:
            k = self._table[i]
            if k == key or k is None:
                return i
            else:
                i += 1
                if i == self._nslot:
                    i = 0

    def _load_factor(self):
        return self._nelem / self._nslot

    def _resize(self):
        oldtable = self._table
        self._nslot *= 2
        self._table = [None] * self._nslot
        for key in oldtable:
            if key is None or key is self.TOMBSTONE:
                continue
            self.insert(key)
