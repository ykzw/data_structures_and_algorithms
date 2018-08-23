#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def python(text, pattern):
    indices = []
    try:
        i = 0
        while True:
            i = text.index(pattern, i)
            indices.append(i)
            i += 1
    except ValueError:
        pass
    return indices
