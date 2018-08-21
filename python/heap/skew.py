#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import operator


class SkewHeap:
    """A skew min heap"""

    class Node:
        __slots__ = ['key', 'id_', 'parent', 'left', 'right']

        def __init__(self, key, id_):
            self.key = key
            self.id_ = id_
            self.parent = None
            self.left = None
            self.right = None

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
        self.root = self._merge_trees(self.root.left, self.root.right)
        return ret

    def decrease_key(self, id_, newkey):
        node = self.id2node[id_]
        node.key = newkey
        parent = node.parent
        while parent and node < parent:
            self._exchange_nodes(node, parent)
            parent = node.parent

    def _merge_trees(self, u, v):
        if not u:
            return v
        elif not v:
            return u

        if not (u < v):
            u, v = v, u
        tmp = u.right
        u.right = u.left
        u.left = self._merge_trees(v, tmp)
        return u

    def _construct(self, A):
        for key, id_ in A:
            self.insert(key, id_)

    def _exchange_nodes(self, u, v):
        u.key, v.key = v.key, u.key
        u.id_, v.id_ = v.id_, u.id_

    def __bool__(self):
        return bool(self.root)
