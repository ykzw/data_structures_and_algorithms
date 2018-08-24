#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import unittest
import collections

import disjointset


class DisjointSetTestCase:
    def setUp(self):
        self.n = 10 ** 3
        self.keys = list(range(self.n))
        self.ds = self.ds_type()
        for k in self.keys:
            self.ds.make_set(k)

    def test_make_set(self):
        refset = set(self.keys)
        for k in self.keys:
            s = self.ds.find_set(k)
            refset.remove(s)
        # refset should be empty
        self.assertFalse(refset)

    def test_union(self):
        correct_sets = [{k} for k in self.keys]
        for i in range(self.n - 1):
            s1, s2 = disjointset.pop_two_sets(correct_sets)
            correct_sets.append(s1 | s2)

            m1 = disjointset.take_one_elem(s1)
            m2 = disjointset.take_one_elem(s2)
            self.ds.union(m1, m2)

            sets = collections.defaultdict(set)
            for i in range(self.n):
                k = self.ds.find_set(i)
                sets[k].add(i)
            sets = sorted(tuple(sorted(s)) for s in sets.values())

            refsets = sorted(tuple(sorted(s)) for s in correct_sets)
            self.assertEqual(sets, refsets)


class LinkedListDisjointSetsTestCase(DisjointSetTestCase, unittest.TestCase):
    ds_type = disjointset.LinkedListDisjointSets


class DisjointSetForestTestCase(DisjointSetTestCase, unittest.TestCase):
    ds_type = disjointset.DisjointSetForest


class DisjointPythonSetsTestCase(DisjointSetTestCase, unittest.TestCase):
    ds_type = disjointset.DisjointPythonSets
