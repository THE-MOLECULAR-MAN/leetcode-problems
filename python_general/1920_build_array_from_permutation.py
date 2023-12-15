#!/usr/bin/python3
# Tim H 2023
# https://leetcode.com/problems/build-array-from-permutation/description/
# Runtime: beats	%
# Memory:  beats	%
"""docstring"""


class Solution:
    """docstring"""

    def buildArray(self, nums: list[int]) -> list[int]:
        """docstring"""
        # lambda function is prob fastest
        # pre-allocate array for speed
        # ans = [0] * len()

        ans = []
        for val in nums:
            ans.append(nums[val])

        return ans
