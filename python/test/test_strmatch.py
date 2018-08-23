#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

import strmatch


class StrMatchTestCase(unittest.TestCase):
    def setUp(self):
        self.n = 10 ** 3
        self.m_range = (1, 100)
        self.alphabet = 'atcg'
        self.text = strmatch.random_string(self.alphabet, self.n)

    def _test(self, func):
        for m in range(*self.m_range):
            pattern = strmatch.random_string(self.alphabet, m)
            for i in func(self.text, pattern):
                self.assertTrue(strmatch.is_valid_shift(self.text, pattern, i))

    def test_python(self):
        self._test(strmatch.python)

    def apply_alphabet(self, func):
        def wrapper(text, pattern):
            return func(text, pattern, self.alphabet)
        return wrapper

    def test_rabin_karp(self):
        f = self.apply_alphabet(strmatch.rabin_karp)
        self._test(f)

    def test_automaton(self):
        f = self.apply_alphabet(strmatch.automaton)
        self._test(f)

    def test_kmp(self):
        self._test(strmatch.kmp)
