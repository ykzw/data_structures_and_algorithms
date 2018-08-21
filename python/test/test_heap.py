#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import unittest

import heap


class BinaryHeapTestCase(unittest.TestCase):
    def setUp(self):
        self.n = 10 ** 3
        self.keys = list(range(self.n))

    def test_construct(self):
        h = heap.BinaryHeap(self.keys)
        self.check_heap_property(h)

    def test_insert(self):
        h = heap.BinaryHeap()
        for k in self.keys:
            h.insert(k)
            self.check_heap_property(h)

    def test_extract(self):
        h = heap.BinaryHeap(self.keys)
        keys = []
        while h:
            keys.append(h.extract())
        self.assertEqual(sorted(keys), keys)

    def test_change_key(self):
        h = heap.BinaryHeap(self.keys)
        for i, k in enumerate(h.A):
            if i % 2 == 0:
                h.change_key(i, k - 10)
            else:
                h.change_key(i, k + 10)
            self.check_heap_property(h)

    def check_heap_property(self, h):
        n = len(h)
        for i, k in enumerate(h.A):
            parent = (i - 1) // 2
            # Parent is smaller
            if i > 0:
                self.assertLessEqual(h.A[parent], k)
            # Children are larger
            left = 2 * i + 1
            if left < n:
                self.assertLessEqual(k, h.A[left])
            right = 2 * i + 2
            if right < n:
                self.assertLessEqual(k, h.A[right])
