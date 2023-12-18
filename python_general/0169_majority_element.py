#!/usr/bin/python3
# Tim H 2023
# https://leetcode.com/problems/majority-element/
# Runtime: beats	87%
# Memory:  beats	51%
"""docstring"""

from collections import Counter


class Solution:
    """docstring"""

    def majorityElement(self, nums: list[int]) -> int:
        """docstring"""
        return Counter(nums).most_common(1)[0][0]
