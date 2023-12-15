#!/usr/bin/python3
# Tim H 2023
# https://leetcode.com/problems/single-number/
# Runtime: beats	%
# Memory:  beats	%
"""docstring"""


class Solution:
    """docstring"""

    def singleNumber(self, nums: List[int]) -> int:
        """docstring"""
        nums.sort()
        i = 0
        while i < len(nums):
            if i == len(nums) - 1:
                return nums[i]
            if nums[i] != nums[i+1]:
                return nums[i]
            i += 2
        return null
