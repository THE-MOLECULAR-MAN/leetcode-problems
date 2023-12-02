#!/usr/bin/python3
# Tim H 2023
# https://leetcode.com/problems/two-sum/description/
# Runtime:
# Memory:
""" module docstring """


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for outer_iter in range(len(nums)):
            for inner_iter in range(outer_iter+1, len(nums)):
                if nums[outer_iter] + nums[inner_iter] == target:
                    return [outer_iter, inner_iter]
        return []
