#!/usr/bin/python3
# Tim H 2023
# https://leetcode.com/problems/concatenation-of-array/
import numpy as np


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # return np.concatenate(nums,nums]
        return nums.extend(nums)
