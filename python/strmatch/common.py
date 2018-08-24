#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import string
import itertools


def is_valid_shift(text, pattern, s):
    m = len(pattern)
    for i in range(m):
        if text[s + i] != pattern[i]:
            return False
    return True


def random_string(alphabet, n):
    return ''.join(random.choices(alphabet, k=n))
