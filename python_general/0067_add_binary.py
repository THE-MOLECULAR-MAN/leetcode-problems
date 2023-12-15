#!/usr/bin/python3
# Tim H 2023
# https://leetcode.com/problems/add-binary/
# Runtime: beats	%
# Memory:  beats	%
"""docstring"""


class Solution:
    """docstring"""

    def addBinary(self, a: str, b: str) -> str:
        """docstring"""
        sum_dec = int(a, base=2) + int(b, base=2)
        return bin(sum_dec).format(10)[2:]
