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
