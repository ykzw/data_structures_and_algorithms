#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Disjoint-set data structures

Common interface:
* Constructor()
  - Create an empty structure

* make_set(member)
  - Make a set only consisting of "member"
  - Assume "member" is not included in the sets

* union(m1, m2)
  - Merge two sets for "m1" and "m2"
  - Return True if the sets are merged
  - Return False otherwise (i.e., m1 and m2 are already in the same set)

* find_set(member)
  - Return a representative member of the set containing "member"

"""

from .linkedlist import LinkedListDisjointSets
from .forest import DisjointSetForest
from .python import DisjointPythonSets
from .util import *
