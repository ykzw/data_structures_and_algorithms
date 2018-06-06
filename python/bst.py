#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""The binary search tree and its variants"""


class BinarySearchTree:
    """The binary search tree based on Chapter 12 of Introduction to Algorithms by Cormen et al."""
    class Node:
        __slots__ = ['key', 'left', 'right', 'parent']

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

    def height(self):
        """Return the height in O(n) time."""
        def rec(node):
            if node is None:
                return 0
            else:
                return max(rec(node.left), rec(node.right)) + 1
        return rec(self.root)


class RedBlackTree:
    """The red-black tree based on Chapter 13 of Introduction to Algorithms by Cormen et al."""
    class CNode:
        __slots__ = ['key', 'children', 'parent', 'red']

        def __init__(self, key=None, left=None, right=None, parent=None, red=True):
            self.key = key
            self.children = [left, right]
            self.parent = parent
            # https://github.com/ActiveState/code/tree/master/recipes/Python/576817_Red_black_tree
            self.red = red

        @property
        def left(self):
            return self.children[0]

        @left.setter
        def left(self, x):
            self.children[0] = x

        @property
        def right(self):
            return self.children[1]

        @right.setter
        def right(self, x):
            self.children[1] = x

        def is_nil(self):
            return self is RedBlackTree.NIL

        def is_child(self, i):
            if i == 0:
                return self.is_left_child()
            else:
                return self.is_right_child()

        def is_left_child(self):
            return (self.parent is not None) and (self.parent.left is self)

        def is_right_child(self):
            return (self.parent is not None) and (self.parent.right is self)

        def __lt__(self, x):
            return self.key < x.key

        def __eq__(self, x):
            return self.key == x.key


    NIL = CNode(red=False)

    def __init__(self):
        self.root = self.NIL

    def search(self, k):
        x = self.root
        while (not x.is_nil()) and k != x.key:
            x = self._search_down(x, k)
        return x

    def _search_down(self, x, k):
        i = 1 - (k < x.key)
        return x.children[i]

    def _set_child(self, y, z):
        z.parent = y
        if y.is_nil():
            self.root = z
        elif z < y:
            y.left = z
        else:
            y.right = z

    def _rotate(self, x, i):
        j = i ^ 1
        y = x.children[j]
        x.children[j] = y.children[i]
        if not y.children[i].is_nil():
            y.children[i].parent = x
        y.parent = x.parent
        if x.parent.is_nil():
            self.root = y
        elif x.is_left_child():
            x.parent.left = y
        else:
            x.parent.right = y
        y.children[i] = x
        x.parent = y

    def _left_rotate(self, x):
        self._rotate(x, 0)

    def _right_rotate(self, x):
        self._rotate(x, 1)

    def insert(self, k):
        z = self.CNode(k)
        return self._insert(z)

    def _insert(self, z):
        y = self.NIL
        x = self.root
        while not x.is_nil():
            if x == z:
                return False
            y = x
            x = self._search_down(x, z.key)
        self._set_child(y, z)

        z.left = z.right = self.NIL
        z.red = True
        self._insert_fixup(z)
        return True

    def _insert_fixup(self, z):
        while z.parent.red:
            if z.parent.is_left_child():
                z = self._insert_fixup_internal(z, 0)
            else:
                z = self._insert_fixup_internal(z, 1)

        self.root.red = False

    def _insert_fixup_internal(self, z, i):
        j = 1 - i
        y = z.parent.parent.children[j]
        if y.red:
            z.parent.red = False
            y.red = False
            z.parent.parent.red = True
            z = z.parent.parent
        else:
            if z.is_child(j):
                z = z.parent
                self._rotate(z, i)
            z.parent.red = False
            z.parent.parent.red = True
            self._rotate(z.parent.parent, j)
        return z

    def delete(self, k):
        z = self.search(k)
        if z.is_nil():
            return False
        else:
            self._delete(z)
            return True

    def _delete(self, z):
        y = z
        y_was_red = y.red
        if z.left.is_nil():
            x = z.right
            self._transplant(z, z.right)
        elif z.right.is_nil():
            x = z.left
            self._transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_was_red = y.red
            x = y.right
            if y.parent is z:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self._transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.red = z.red

        if not y_was_red:
            self._delete_fixup(x)

    def _delete_fixup(self, x):
        while (x is not self.root) and (not x.red):
            if x.is_left_child():
                x = self._delete_fixup_internal(x, 0)
            else:
                x = self._delete_fixup_internal(x, 1)
        x.red = False

    def _delete_fixup_internal(self, x, i):
        j = 1 - i
        w = x.parent.children[j]
        if w.red:
            w.red = False
            x.parent.red = True
            self._rotate(x.parent, i)
            w = x.parent.children[j]
        if not w.children[i].red and not w.children[j].red:
            w.red = True
            x = x.parent
        else:
            if not w.children[j].red:
                w.children[i].red = False
                w.red = True
                self._rotate(w, j)
                w = x.parent.children[j]
            w.red = x.parent.red
            x.parent.red = False
            w.children[j].red = False
            self._rotate(x.parent, i)
            x = self.root
        return x

    def _transplant(self, u, v):
        if u.parent.is_nil():
            self.root = v
        elif u.is_left_child():
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def minimum(self, x):
        if x.is_nil():
            return x

        while not x.left.is_nil():
            x = x.left
        return x

    def height(self):
        def rec(node):
            if node.is_nil():
                return 0
            else:
                return max(rec(node.left), rec(node.right)) + 1
        return rec(self.root)


def _benchmark(tree_type, keys):
    import time
    t = tree_type()
    begin = time.time()
    for k in keys:
        t.insert(k)
    end = time.time()

    print(tree_type.__name__)
    print('* Insert in {:.3} s'.format(end - begin))
    print('* Height is {}'.format(t.height()))

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
    _benchmark(RedBlackTree, keys)


if __name__ == "__main__":
    benchmark()
