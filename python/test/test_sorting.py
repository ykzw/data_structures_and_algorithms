#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import functools
import unittest

import sorting


class TestMeta(type):
    def __new__(cls, name, bases, attrs):
        def test(sort_func):
            @functools.wraps(sort_func)
            def f(self):
                sort_func(self.A)
                self.assertEqual(self.A, self.ref)
            return f

        for name in dir(sorting):
            if 'sort' in name:
                func = getattr(sorting, name)
                attrs['test_' + name] = test(func)

        return type.__new__(cls, name, bases, attrs)


class SortTestCase(unittest.TestCase, metaclass=TestMeta):
    @classmethod
    def setUpClass(cls):
        n = 2 ** 10
        cls.array = [random.randrange(n * n) for _ in range(n)]
        cls.ref = sorted(cls.array)

    def setUp(self):
        self.A = self.array[:]
