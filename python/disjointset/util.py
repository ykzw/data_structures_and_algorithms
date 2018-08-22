#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


def take_one_elem(set):
    return next(iter(set))


def pop_two_sets(sets):
    n = len(sets)
    i = random.randrange(n)
    j = random.randrange(i + 1, n + i) % n
    s1 = sets.pop(i)
    s2 = sets.pop(j - (i < j))
    return (s1, s2)
