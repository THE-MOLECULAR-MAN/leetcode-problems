#!/usr/bin/python3
# Tim H 2023
# https://leetcode.com/problems/move-zeroes/
# Runtime:  beats 5%
# Memory:   beats 73%
"""docstring"""


class Solution:
    """docstring"""

    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # #indices_of_zeros = [i for i, x in enumerate(nums) if x == 0]
        # [i for i in range(len(my_list)) if my_list[i] == my_element]
        # #print(indices)
        # #r = range(len(nums))
        # L = len(nums)

        # nums = [e for e, x in nums if x != 0 ]
        # print(nums)
        # num_zeros = L - len(nums)
        # print(num_zeros)
        # nums = nums.append([0] * num_zeros)
        # # print(x)

        try:
            last = len(nums) - 1
            # i = 0
            while last > 0:
                nums.remove(0)
                nums.append(0)
                last -= 1

        except ValueError:
            return None

        return None
