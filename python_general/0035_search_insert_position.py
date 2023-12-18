#!/usr/bin/python3
# Tim H 2023
# https://leetcode.com/problems/search-insert-position/
# Runtime:  beats 58%
# Memory:   beats 39%
"""docstring"""

import bisect


class Solution:
    """docstring"""

    def searchInsert(self, nums: list[int], target: int) -> int:
        """docstring"""
        return bisect.bisect_left(nums, target)
