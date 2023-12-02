#!/usr/bin/python3
# Tim H 2023
# https://leetcode.com/problems/number-of-1-bits/description/

import operator as op

class Solution:
    def hammingWeight(self, n: int) -> int:
        return op.countOf(bin(n), "1")
