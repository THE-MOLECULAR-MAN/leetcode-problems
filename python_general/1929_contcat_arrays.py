#!/usr/bin/python3
# Tim H 2023
# https://leetcode.com/problems/concatenation-of-array/description/
# Runtime:
# Memory:
"""docstring"""

# import numpy as np


class Solution:
    """docstring"""

    def getConcatenation(self, nums: List[int]) -> List[int]:
        """docstring"""
        # return np.concatenate(nums,nums]
        return nums.extend(nums)
