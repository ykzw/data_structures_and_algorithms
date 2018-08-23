#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""A B-tree"""

import bisect


class BTree:
    class Node:
        def __init__(self, keys=None, is_leaf=True, children=None):
            if not keys:
                keys = []
            self.keys = keys
            self.is_leaf = is_leaf
            if not children:
                children = []
            self.children = children

        def __len__(self):
            return len(self.keys)

        def __iter__(self):
            if self.is_leaf:
                yield from self.keys
            else:
                for c in self.children:
                    yield from c

    def __init__(self, t=2**10):
        self.t = t
        self.root = self.Node()

    def search(self, k):
        r = self.root
        while True:
            i = bisect.bisect_left(r.keys, k)
            if i < len(r) and r.keys[i] == k:
                return True
            if r.is_leaf:
                return False
            r = r.children[i]

    def _split_child(self, x, i):
        # Move the second half of y to a new node z
        y = x.children[i]
        median = y.keys[self.t - 1]
        z = self.Node(is_leaf=y.is_leaf)
        y.keys, z.keys = y.keys[:self.t - 1], y.keys[self.t:]
        if not y.is_leaf:
            y.children, z.children = y.children[:self.t], y.children[self.t:]

        # Move up the median in y.keys to the parent x
        x.children.insert(i + 1, z)
        x.keys.insert(i, median)

    def insert(self, k):
        if self.search(k):
            return False
        r = self.root
        if len(r) == 2 * self.t - 1:
            # If the root is full,
            # create a new root and
            # let the original root be a child of the new root.
            self.root = self.Node(is_leaf=False, children=[r])
            # Then split the original root
            self._split_child(self.root, 0)
            self._insert_nonfull(self.root, k)
        else:
            self._insert_nonfull(r, k)
        return True

    def _insert_nonfull(self, x, k):
        i = bisect.bisect_left(x.keys, k)
        if x.is_leaf:
            x.keys.insert(i, k)
        else:
            if len(x.children[i]) == 2 * self.t - 1:
                self._split_child(x, i)
                if k > x.keys[i]:
                    i += 1
            self._insert_nonfull(x.children[i], k)

    def delete(self, k):
        return self._delete_nonhalf(self.root, k)

    def _delete_nonhalf(self, x, k):
        i = bisect.bisect_left(x.keys, k)
        if i < len(x) and x.keys[i] == k:
            if x.is_leaf:
                x.keys.pop(i)
            elif len(x.children[i]) >= self.t:
                # Can be improved but seems troublesome
                k2 = self._predecessor(x.children[i], k)
                self._delete_nonhalf(x.children[i], k2)
                x.keys[i] = k2
            elif len(x.children[i + 1]) >= self.t:
                # Can be improved but seems troublesome
                k2 = self._sucessor(x.children[i + 1], k)
                self._delete_nonhalf(x.children[i + 1], k2)
                x.keys[i] = k2
            else:
                self._merge_node(x, i)
                y = x.children[i]
                self._delete_nonhalf(y, k)
        elif x.is_leaf:
            return False
        else:
            y = x.children[i]
            if len(y) == self.t - 1:
                if i > 0 and len(x.children[i - 1]) >= self.t:
                    left_sib = x.children[i - 1]
                    y.keys.insert(0, x.keys[i - 1])
                    x.keys[i - 1] = left_sib.keys.pop()
                    if not left_sib.is_leaf:
                        y.children.insert(0, left_sib.children.pop())
                elif i < len(x) and len(x.children[i + 1]) >= self.t:
                    right_sib = x.children[i + 1]
                    y.keys.append(x.keys[i])
                    x.keys[i] = right_sib.keys.pop(0)
                    if not right_sib.is_leaf:
                        y.children.append(right_sib.children.pop(0))
                else:
                    if i < len(x):
                        self._merge_node(x, i)
                    else:
                        y = x.children[i - 1]
                        self._merge_node(x, i - 1)
            self._delete_nonhalf(y, k)
        if not self.root.is_leaf and len(self.root) == 0:
            self.root = self.root.children[0]
        return True

    def _merge_node(self, x, i):
        """Merge the (i+1)-th child of x to the i-th child"""
        y = x.children[i]
        z = x.children.pop(i + 1)
        y.keys.append(x.keys.pop(i))
        y.keys.extend(z.keys)
        y.children.extend(z.children)

    def _predecessor(self, y, k):
        while not y.is_leaf:
            y = y.children[-1]
        return y.keys[-1]

    def _sucessor(self, y, k):
        while not y.is_leaf:
            y = y.children[0]
        return y.keys[0]

    def height(self):
        h = 1
        r = self.root
        while not r.is_leaf:
            r = r.children[0]
            h += 1
        return h

    def __iter__(self):
        yield from self.root
