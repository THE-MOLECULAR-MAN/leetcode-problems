#!/usr/bin/python3
# Tim H 2023
# UNFINISHED
# https://leetcode.com/problems/merge-sorted-array/
"""docstring"""

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if len(nums1) == 0: 
            nums1 = nums2

        for i1, v1 in enumerate(nums1):            
            if len(nums2) == 0:
                return None
            
            i2 = 0
            while (i2 < len(nums2)):
                if nums2[i2] >= v1:
                    nums1.insert(nums2[i2],i1)
                i2 += 1
            # del nums2[0:i2]
            nums2 = nums2[i2:]
            

# nums1 = [1, 2, 3, 0, 0, 0]
# nums2 = [2, 5, 6]
# nums1L = len(nums1)
# nums2L = len(nums2)


# Solution().merge(nums1, nums1L, nums2, nums2L)
# print(nums1)

            

nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
nums1L = len(nums1)
nums2L = len(nums2)


Solution().merge(nums1, nums1L, nums2, nums2L)
print(nums1)
