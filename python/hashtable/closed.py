#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class ClosedHashTable:
    def __init__(self):
        self._nelem = 0
        self._nslot = 2
        self._table = [[] for _ in range(self._nslot)]

    def insert(self, key):
        slot = self._get_slot(key)
        try:
            slot.index(key)
            return False
        except ValueError:
            slot.append(key)
            self._nelem += 1
            if self._load_factor() > 4:
                self._resize()
            return True

    def search(self, key):
        slot = self._get_slot(key)
        try:
            slot.index(key)
            return True
        except ValueError:
            return False

    def delete(self, key):
        slot = self._get_slot(key)
        try:
            slot.remove(key)
            self._nelem -= 1
            return True
        except ValueError:
            return False

    def _load_factor(self):
        return self._nelem / self._nslot

    def _get_slot(self, key):
        h = hash(key) % self._nslot
        return self._table[h]

    def _resize(self):
        oldtable = self._table
        self._nslot *= 2
        self._table = [[] for _ in range(self._nslot)]
        for slot in oldtable:
            for key in slot:
                self.insert(key)
