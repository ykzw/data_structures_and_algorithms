#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


class FibonacciHeap:
    """A fibonacci min heap based on the book by Cormen et al."""

    class Node:
        __slots__ = ['key', 'id_', 'degree', 'child', 'mark', 'left', 'right', 'parent']

        def __init__(self, key, id_):
            self.key = key
            self.id_ = id_
            self.degree = 0
            self.child = None
            self.mark = False
            self.left = self
            self.right = self
            self.parent = None

        def add_child(self, c):
            if self.child:
                c.right = self.child
                c.left = self.child.left
                c.left.right = c
                c.right.left = c
            else:
                c.left = c.right = c
            self.child = c
            self.degree += 1
            c.parent = self
            c.mark = False

        def children(self):
            if self.child:
                yield self.child
                c = self.child
                while c.right is not self.child:
                    yield c.right
                    c = c.right

        def __lt__(self, other):
            return self.key < other.key

    def __init__(self, A=None):
        self.min = None
        self.roots = []
        self.id2node = {}
        if A:
            self._construct(A)

    def merge(self, other):
        self.roots.extend(other.roots)
        self.min = min(self.min, other.min)
        self.id2node.update(other.id2node)

    def insert(self, key, id_):
        node = self.Node(key, id_)
        self.id2node[id_] = node
        self._append_root(node)

    def extract(self):
        z = self.min
        if z:
            self.roots.remove(z)
            for c in z.children():
                self.roots.append(c)
                c.parent = None
            if not self.roots:  # no siblings
                self.min = None
            else:
                self.min = self.roots[0]
                self._consolidate()
        self.id2node.pop(z.id_)
        return (z.key, z.id_)

    def decrease_key(self, id_, newkey):
        node = self.id2node[id_]
        self._decrease_key(node, newkey)

    def _append_root(self, u):
        if self.min is None:
            self.roots = [u]
            self.min = u
        else:
            self.roots.append(u)
            self.min = min(self.min, u)

    def _consolidate(self):
        A = [None] * (int(math.log(len(self.id2node), 1.618)) + 1)
        tmp = self.roots
        self.roots = []
        for x in tmp:
            while A[x.degree]:
                y = A[x.degree]
                if x > y:
                    x, y = y, x
                A[x.degree] = None
                self._link(y, x)
            A[x.degree] = x
        self.min = None
        for a in A:
            if not a: continue
            self._append_root(a)

    def _link(self, y, x):
        x.add_child(y)

    def _decrease_key(self, x, k):
        x.key = k
        y = x.parent
        if y is not None and x < y:
            self._cut(x, y)
            self._cascading_cut(y)
        if x < self.min:
            self.min = x

    def _cut(self, x, y):
        y.degree -= 1
        if y.degree > 0:
            x.left.right = x.right
            x.right.left = x.left
            y.child = x.right
        else:
            y.child = None
        self.roots.append(x)
        x.parent = None
        x.mark = False

    def _cascading_cut(self, y):
        z = y.parent
        if z is not None:
            if not y.mark:
                y.mark = True
            else:
                self._cut(y, z)
                self._cascading_cut(z)

    def _construct(self, A):
        for key, id_ in A:
            self.insert(key, id_)

    def __getitem__(self, id_):
        return self.id2node[id_].key

    def __contains__(self, id_):
        return id_ in self.id2node

    def __bool__(self):
        return bool(self.id2node)
