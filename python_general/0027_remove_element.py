#!/usr/bin/python3
# Tim H 2023
# https://leetcode.com/problems/remove-element/description/
# Runtime: beats	32%
# Memory:  beats	20%
"""docstring"""


class Solution:
    """docstring"""

    def removeElement(self, nums: list[int], val: int) -> int:
        """docstring"""
        nums[:] = [x for x in nums if x != val]
        return len(nums)
