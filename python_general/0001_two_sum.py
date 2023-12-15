#!/usr/bin/python3
# Tim H 2023
# https://leetcode.com/problems/two-sum/description/
# Runtime: beats:  34%
# Memory:  beats:  59%
"""docstring"""


class Solution:
    """docstring"""

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """docstring"""
        for outer_iter, val_outer in enumerate(nums):
            for inner_iter in range(outer_iter+1, len(nums)):
                if val_outer + nums[inner_iter] == target:
                    return [outer_iter, inner_iter]
        return []
