#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""The binary search tree and its variants"""


class BinarySearchTree:
    """The binary search tree based on Chapter 12 of Introduction to Algorithms by Cormen et al."""
    class Node:
        def __init__(self, key=None, left=None, right=None, parent=None):
            self.key = key
            self.left = left
            self.right = right
            self.parent = parent

        def is_left_child(self):
            """Return true if this node is the left child of the parent."""
            return (self.parent is not None) and (self.parent.left is self)

        def is_right_child(self):
            """Return true if this node is the right child of the parent."""
            return (self.parent is not None) and (self.parent.right is self)

        def __lt__(self, y):
            return self.key < y.key

        def __eq__(self, y):
            return self.key == y.key


    def __init__(self):
        self.root = None

    def search(self, k):
        """Return the node with key k if it exists; otherwise return None."""
        x = self.root
        while x is not None and k != x.key:
            x = self._search_down(x, k)
        return x

    def _search_down(self, x, k):
        if k < x.key:
            return x.left
        else:
            return x.right

    def insert(self, k):
        """Insert a new key k and return True; if it already exists, return False."""
        z = self.Node(k)
        return self._insert(z)

    def _insert(self, z):
        """Insert a new node z."""
        y = None
        x = self.root
        while x:
            if x == z:
                return False
            y = x
            x = self._search_down(x, z.key)
        self._set_child(y, z)
        return True

    def _set_child(self, y, z):
        """Set z to the child of y."""
        z.parent = y
        if y is None:
            self.root = z
        elif z < y:
            y.left = z
        else:
            y.right = z

    def minimum(self, x):
        """Return the node with the minimum key in the subtree rooted at x."""
        while x.left:
            x = x.left
        return x

    def maximum(self, x):
        """Return the node with the maximum key in the subtree rooted at x."""
        while x.right:
            x = x.right
        return x

    def delete(self, k):
        """Delete a node with key k if it exists and return True; otherwise just return False."""
        z = self.search(k)
        if z:
            self._delete(z)
            return True
        else:
            return False

    def _delete(self, z):
        """Delete an existing node z."""
        if z.left is None:
            self._transplant(z, z.right)
        elif z.right is None:
            self._transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            if y.parent is not z:
                self._transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self._transplant(z, y)
            y.left = z.left
            y.left.parent = y

    def _transplant(self, u, v):
        """Replace the subtree rooted at u with the subtree rooted at v."""
        if u.parent is None:  # If u is the root
            self.root = v
        elif u.is_left_child():
            u.parent.left = v
        else:
            u.parent.right = v

        if v:
            v.parent = u.parent


def _benchmark(tree_type, keys):
    import time
    t = tree_type()
    begin = time.time()
    for k in keys:
        t.insert(k)
    end = time.time()

    print(tree_type.__name__)
    print('* Insert in {:.3} s'.format(end - begin))

    begin = time.time()
    for k in keys:
        t.search(k)
    end = time.time()
    print('* Search in {:.3} s'.format(end - begin))

    begin = time.time()
    for k in keys:
        t.delete(k)
    end = time.time()
    print('* Delete in {:.3} s'.format(end - begin))
    print()

def benchmark():
    import random
    n = 10 ** 5
    keys = list(range(n))
    random.shuffle(keys)

    print('=====', n, 'keys =====\n')

    _benchmark(BinarySearchTree, keys)


if __name__ == "__main__":
    benchmark()
