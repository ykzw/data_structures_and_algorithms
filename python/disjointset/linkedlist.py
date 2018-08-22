#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Section 21.2 of Introduction to Algorithms by Cormen et al.
class LinkedListDisjointSets:
    class SetObject:
        def __init__(self, head=None, tail=None):
            self.length = 1
            self.head = head
            self.tail = tail

    class Node:
        def __init__(self, member, set_obj=None, next_=None):
            self.member = member
            self.set_obj = set_obj
            self.next_ = next_

    def __init__(self):
        self.mem2node = {}

    def make_set(self, member):
        node = self.Node(member)
        self.mem2node[member] = node
        node.set_obj = self.SetObject(node, node)

    def union(self, m1, m2):
        s1 = self.mem2node[m1].set_obj
        s2 = self.mem2node[m2].set_obj
        if s1 == s2:
            return False

        # Merge s2 to s1
        if s1.length < s2.length:
            # Make s2 smaller
            s1, s2 = s2, s1
        s1.length += s2.length
        # Update set_obj of the s2 head
        x = s2.head
        x.set_obj = s1
        # Update the next of the current s1 tail
        tail = s1.tail
        tail.next_ = x
        # Update set_obj of s2 nodes other than the head
        while x.next_:
            x = x.next_
            x.set_obj = s1
        # Update the s1 tail
        s1.tail = x
        return True

    def find_set(self, member):
        return self._find_set_of_node(self.mem2node[member])

    def _find_set_of_node(self, x):
        return x.set_obj.head.member
