#!/usr/bin/python3
# Tim H 2023
# https://leetcode.com/problems/number-of-1-bits/description/
"""docstring"""

import operator as op


class Solution:
    """docstring"""

    def hammingWeight(self, n: int) -> int:
        """docstring"""
        return op.countOf(bin(n), "1")
