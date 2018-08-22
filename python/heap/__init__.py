#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Heap data structures

Common interface:
* Constructor(A=None)
  - Construct a heap from "A" if it's supplied
  - Otherwise the heap is empty
  - "A" is a sequence of key-id pairs

* insert(key, id)
  - Insert a pair of "key" and its "id" to the heap
  - e.g., "key" is a priority and "id" is some ID

* extract()
  - Remove the pair with the minimum key from the heap and return it

* decrease_key(id, newkey)
  - Decrease the key of "id" to "newkey"
  - Assume "newkey" is less than the current key

* merge(other)
  - Merge the "other" heap into the heap

"""

from .binary import BinaryHeap
from .binomial import BinomialHeap
from .pairing import PairingHeap
from .skew import SkewHeap
from .fibonacci import FibonacciHeap
