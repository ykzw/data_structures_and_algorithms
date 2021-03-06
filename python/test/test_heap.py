#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import unittest

import heap


class BinaryHeapTestCase(unittest.TestCase):
    def setUp(self):
        self.n = 10 ** 3
        keys = list(range(self.n))
        self.items = [(k, k) for k in keys]

    def test_construct(self):
        h = heap.BinaryHeap(self.items)
        self.check_heap_property(h)

    def test_insert(self):
        h = heap.BinaryHeap()
        for k, id_ in self.items:
            h.insert(k, id_)
            self.check_heap_property(h)

    def test_extract(self):
        h = heap.BinaryHeap(self.items)
        keys = []
        while h:
            keys.append(h.extract()[0])
        self.assertEqual(sorted(keys), keys)

    def test_decrease_key(self):
        h = heap.BinaryHeap(self.items)
        for k, id_ in self.items:
            h.decrease_key(id_, k - 100)
            self.check_heap_property(h)

    def test_merge(self):
        h1 = heap.BinaryHeap(self.items)
        h2 = heap.BinaryHeap((k + self.n, id_ + self.n) for k, id_ in self.items)
        h1.merge(h2)
        self.check_heap_property(h1)

    def check_heap_property(self, h):
        n = len(h)
        for i, (k, id_) in enumerate(h.A):
            parent = (i - 1) // 2
            # Parent is smaller
            if parent >= 0:
                self.assertLessEqual(h.A[parent][0], k)
            # Children are larger
            left = 2 * i + 1
            if left < n:
                self.assertLessEqual(k, h.A[left][0])
            right = 2 * i + 2
            if right < n:
                self.assertLessEqual(k, h.A[right][0])



class MergeableHeapTest:
    def setUp(self):
        self.n = 10 ** 3
        self.keys = list(range(self.n))
        self.items = [(k, k) for k in self.keys]

    def test_heap(self):
        h = self.heap_type(self.items)
        self.check_heap(h, self.keys)

    def test_merge(self):
        h1 = self.heap_type(self.items)
        h2 = self.heap_type((k + self.n, id_ + self.n) for k, id_ in self.items)
        h1.merge(h2)
        refkeys = self.keys + [k + self.n for k in self.keys]
        self.check_heap(h1, refkeys)

    def test_decrease_key(self):
        h = self.heap_type(self.items)
        for key, id_ in self.items[:100]:
            h.decrease_key(id_, -key - 1)
        refkeys = [-k - 1 for k in self.keys[:100]] + self.keys[100:]
        refkeys.sort()
        self.check_heap(h, refkeys)

    def check_heap(self, h, refkeys):
        # Keys should be extracted in ascending order
        keys = []
        while h:
            keys.append(h.extract()[0])
        self.assertEqual(refkeys, keys)
        # Check whether nodes have been removed
        self.assertTrue(not h)
        self.assertTrue(not h.id2node)


class BinomialHeapTestCase(MergeableHeapTest, unittest.TestCase):
    heap_type = heap.BinomialHeap


class PairingHeapTestCase(MergeableHeapTest, unittest.TestCase):
    heap_type = heap.PairingHeap


class SkewHeapTestCase(MergeableHeapTest, unittest.TestCase):
    heap_type = heap.SkewHeap


class FibonacciHeapTestCase(MergeableHeapTest, unittest.TestCase):
    heap_type = heap.FibonacciHeap
