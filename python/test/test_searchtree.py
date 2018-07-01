#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import unittest

import searchtree


class BSTTestCase(unittest.TestCase):
    def setUp(self):
        self.n = 2 ** 10

        self.in_keys = list(range(self.n))
        random.shuffle(self.in_keys)

        self.t = searchtree.BinarySearchTree()
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
            self.assertEqual(self.t.search(k).key, k)
        for k in self.out_keys:
            self.assertEqual(self.t.search(k), None)

    def test_delete(self):
        for k in self.out_keys:
            self.assertFalse(self.t.delete(k))
        for k in self.in_keys:
            self.assertTrue(self.t.delete(k))
        self.assertEqual(self.t.root, None)


class RBTTestCase(unittest.TestCase):
    def setUp(self):
        self.n = 2 ** 10

        self.in_keys = list(range(self.n))
        random.shuffle(self.in_keys)

        self.t = searchtree.RedBlackTree()
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
            self.assertEqual(self.t.search(k).key, k)
        for k in self.out_keys:
            self.assertEqual(self.t.search(k), searchtree.RedBlackTree.NIL)

    def test_delete(self):
        for k in self.out_keys:
            self.assertFalse(self.t.delete(k))
        for k in self.in_keys:
            self.assertTrue(self.t.delete(k))
        self.assertTrue(self.t.root.is_nil())
