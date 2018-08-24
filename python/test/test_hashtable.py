#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import unittest
import collections

import hashtable


class HashTableTestCase:
    def setUp(self):
        self.n = 10 ** 3
        self.keys = list(range(self.n))
        self.ht = self.ht_type()

    def test_insert(self):
        for k in self.keys:
            self.assertFalse(self.ht.search(k))
            self.assertTrue(self.ht.insert(k))
            self.assertTrue(self.ht.search(k))
            self.assertFalse(self.ht.insert(k))

    def test_delete(self):
        for k in self.keys:
            self.ht.insert(k)

        for k in self.keys:
            self.assertTrue(self.ht.search(k))
            self.assertTrue(self.ht.delete(k))
            self.assertFalse(self.ht.search(k))
            self.assertFalse(self.ht.delete(k))


class ClosedHashTableTestCase(HashTableTestCase, unittest.TestCase):
    ht_type = hashtable.ClosedHashTable


class LinearHashTableTestCase(HashTableTestCase, unittest.TestCase):
    ht_type = hashtable.LinearHashTable


class CuckooHashTableTestCase(HashTableTestCase, unittest.TestCase):
    ht_type = hashtable.CuckooHashTable


class HopscotchHashTableTestCase(HashTableTestCase, unittest.TestCase):
    ht_type = hashtable.HopscotchHashTable


class PythonHashTableTestCase(HashTableTestCase, unittest.TestCase):
    ht_type = hashtable.PythonHashTable
