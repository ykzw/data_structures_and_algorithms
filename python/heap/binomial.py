#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class BinomialHeap:
    """A binomial min heap"""

    class Node:
        def __init__(self, key, id_):
            self.key = key
            self.id_ = id_
            self.parent = None
            self.children = {}

        def add_child(self, c, order):
            self.children[order] = c
            c.parent = self

        def __lt__(self, other):
            return self.key < other.key

        def __le__(self, other):
            return self.key <= other.key

    def __init__(self, A=None):
        self.roots = {}
        self.id2node = {}
        if A:
            self._construct(A)

    def merge(self, other):
        """Merge the "other" heap into self"""
        for order, root in sorted(other.roots.items()):
            while order in self.roots:
                # Merge the trees of the same order
                root = self._merge_trees(root, self.roots[order], order)
                self.roots.pop(order)
                order += 1
            self.roots[order] = root
        self.id2node.update(other.id2node)

    def insert(self, k, id_):
        """Insert an item to the heap"""
        # Create a temporary heap containing a single node with k and id_
        # and merge it into self
        tmpheap = BinomialHeap()
        node = self.Node(k, id_)
        tmpheap.roots[0] = node
        self.id2node[id_] = node
        self.merge(tmpheap)

    def extract(self):
        """Remove and return the item with the minimum key"""
        minroot, order = min((root, order) for order, root in self.roots.items())
        self.roots.pop(order)
        self.id2node.pop(minroot.id_)
        # Merge the children of the removed node into self
        tmpheap = BinomialHeap()
        tmpheap.roots = minroot.children
        self.merge(tmpheap)
        return (minroot.key, minroot.id_)

    def decrease_key(self, id_, newkey):
        """Decrease the key of id_ to k"""
        node = self.id2node[id_]
        node.key = newkey
        parent = node.parent
        while parent and node < parent:
            self._exchange_nodes(node, parent)
            parent = node.parent

    def _merge_trees(self, u, v, order):
        if u <= v:
            u.add_child(v, order)
            return u
        else:
            v.add_child(u, order)
            return v

    def _construct(self, A):
        for k, id_ in A:
            self.insert(k, id_)

    def _exchange_nodes(self, u, v):
        u.key, v.key = v.key, u.key
        u.id_, v.id_ = v.id_, u.id_

    def __bool__(self):
        return bool(self.roots)

    def __len__(self):
        return len(self.id2node)
