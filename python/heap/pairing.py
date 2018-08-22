#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import itertools

from .skew import SkewHeap

class PairingHeap(SkewHeap):
    """A pairing min heap"""

    class Node:
        __slots__ = ['key', 'id_', 'parent', 'children']

        def __init__(self, key, id_):
            self.key = key
            self.id_ = id_
            self.parent = None
            self.children = []

        def add_child(self, node):
            self.children.append(node)
            node.parent = self

        def __lt__(self, other):
            return self.key < other.key

    def extract(self):
        ret = (self.root.key, self.root.id_)
        self.id2node.pop(self.root.id_)
        for c in self.root.children:
            c.parent = None
        self.root = self._merge_list(self.root.children)
        return ret

    def _merge_trees(self, u, v):
        if not u:
            return v
        elif not v:
            return u

        if not (u < v):
            u, v = v, u
        u.add_child(v)
        return u

    def _merge_list(self, trees):
        if len(trees) == 0:
            return None
        elif len(trees) == 1:
            return trees[0]
        else:
            newtrees = []
            it = iter(trees)
            for u, v in itertools.zip_longest(it, it):
                newtrees.append(self._merge_trees(u, v))
            r = newtrees[-1]
            n = len(newtrees)
            for i in range(n - 2, -1, -1):
                u = newtrees[i]
                r = self._merge_trees(u, r)
            return r
