#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class PythonHashTable:
    def __init__(self):
        self._table = set()

    def insert(self, key):
        if key in self._table:
            return False
        else:
            self._table.add(key)
            return True

    def search(self, key):
        return key in self._table

    def delete(self, key):
        try:
            self._table.remove(key)
            return True
        except KeyError:
            return False
