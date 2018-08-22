#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class DisjointSetForest:
    class Node:
        __slots__ = ['member', 'rank', 'parent']

        def __init__(self, member):
            self.member = member
            self.rank = 0
            self.parent = self

    def __init__(self):
        self.mem2node = {}

    def make_set(self, member):
        self.mem2node[member] = self.Node(member)

    def union(self, m1, m2):
        s1, s2 = self._find_set(m1), self._find_set(m2)
        if s1.rank > s2.rank:
            s2.parent = s1
        else:
            s1.parent = s2
            if s1.rank == s2.rank:
                s2.rank += 1

    def find_set(self, member):
        s = self._find_set(member)
        return s.member

    def _find_set(self, member):
        node = self.mem2node[member]
        return self._find_set_of_node(node)

    def _find_set_of_node(self, x):
        if x is not x.parent:
            x.parent = self._find_set_of_node(x.parent)
        return x.parent
