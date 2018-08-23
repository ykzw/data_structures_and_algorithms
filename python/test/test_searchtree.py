#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import unittest

import searchtree


class SearchTreeTest:
    def setUp(self):
        self.n = 2 ** 10

        self.in_keys = list(range(self.n))
        random.shuffle(self.in_keys)

        self.t = self.tree_type()
        for k in self.in_keys:
            self.t.insert(k)

        self.out_keys = list(range(self.n, self.n * 2))

    def test_insert(self):
        for k in self.in_keys:
            self.assertFalse(self.t.insert(k))
        for k in self.out_keys:
            self.assertTrue(self.t.insert(k))

    def test_search(self):
        for k in self.in_keys:
            self.assertTrue(self.t.search(k))
        for k in self.out_keys:
            self.assertFalse(self.t.search(k))

    def test_delete(self):
        for k in self.out_keys:
            self.assertFalse(self.t.delete(k))
        for k in self.in_keys:
            self.assertTrue(self.t.delete(k))
            self.assertFalse(self.t.search(k))
        self.assertFalse(self.t.root)


class BSTTestCase(SearchTreeTest, unittest.TestCase):
    tree_type = searchtree.BinarySearchTree


class RBTTestCase(SearchTreeTest, unittest.TestCase):
    tree_type = searchtree.RedBlackTree


class BTreeTestCase(SearchTreeTest, unittest.TestCase):
    tree_type = searchtree.BTree
