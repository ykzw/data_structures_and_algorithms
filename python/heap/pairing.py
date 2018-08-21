#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import itertools


class PairingHeap:
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

    def __init__(self, A=None):
        self.root = None
        self.id2node = {}
        if A:
            self._construct(A)

    def merge(self, other):
        self.root = self._merge_trees(self.root, other.root)
        self.id2node.update(other.id2node)

    def insert(self, key, id_):
        node = self.Node(key, id_)
        self.id2node[id_] = node
        self.root = self._merge_trees(self.root, node)

    def extract(self):
        ret = (self.root.key, self.root.id_)
        self.id2node.pop(self.root.id_)
        self.root = self._merge_list(self.root.children)
        return ret

    def decrease_key(self, id_, newkey):
        node = self.id2node[id_]
        node.key = newkey
        parent = node.parent
        while parent and node < parent:
            self._exchange_nodes(node, parent)
            parent = node.parent

    @staticmethod
    def _merge_trees(u, v):
        if not u:
            return v
        elif not v:
            return u

        if u < v:
            r = u
            r.add_child(v)
        else:
            r = v
            r.add_child(u)
        return r

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

    def _construct(self, A):
        for key, id_ in A:
            self.insert(key, id_)

    def _exchange_nodes(self, u, v):
        u.key, v.key = v.key, u.key
        u.id_, v.id_ = v.id_, u.id_

    def __bool__(self):
        return bool(self.root)
