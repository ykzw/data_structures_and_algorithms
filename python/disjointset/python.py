#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .util import *


class DisjointPythonSets:
    def __init__(self):
        self.mem2set = {}

    def make_set(self, x):
        self.mem2set[x] = {x}

    def union(self, m1, m2):
        s1, s2 = self.mem2set[m1], self.mem2set[m2]
        if len(s1) < len(s2):
            s1, s2 = s2, s1
        s1.update(s2)
        for mem in s2:
            self.mem2set[mem] = s1

    def find_set(self, x):
        return take_one_elem(self.mem2set[x])
