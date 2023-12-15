#!/usr/bin/python3
# Tim H 2023
# https://leetcode.com/problems/number-of-good-pairs/
# Runtime: beats 86%
# Memory: beats 51%
"""docstring"""


class Solution:
    """docstring"""

    def numIdenticalPairs(self, nums: List[int]) -> int:
        """docstring"""
        ans = 0
        for ind1, val1 in enumerate(nums):
            for val2 in nums[ind1+1:]:
                if val1 == val2:
                    ans += 1
        return ans
