#!/usr/bin/python3
# Tim H 2023
# UNFINISHED
# https://leetcode.com/problems/sqrtx/description/description/
# Runtime: beats	%
# Memory:  beats	%
"""docstring"""

# very very slow: O(n)


def mySqrt(x: int) -> int:
    """docstring"""
    if x == 0:
        return 0
    if x < 3:
        return 1
    i = 2
    while i <= 65535:
        if i * i > x:
            return i-1
        if i * i == x:
            return i
        i += 1
    return None

# def generate_list_of_squares():
#     i = 0
#     ans = []
#     # ans = [[0,0], [1,1], [2,4]]
#     while i * i <= 65536:
#         ans.append(i*i)
#         i += 1
#     return ans



class Solution:
    """other person's solution"""
    def mySqrt(self, x: int) -> int:
        """docstring"""
        if x == 0:
            return 0
        first, last = 1, x
        while first <= last:
            mid = first + (last - first) // 2
            if mid == x // mid:
                return mid
            if mid > x // mid:
                last = mid - 1
            else:
                first = mid + 1
        return last

###############################################################################
#       MAIN
###############################################################################


tests = [0, 1, 2, 3, 4, 15, 16, 17, 65534, 65535]

for test_iter in tests:
    print(str(test_iter) + ' -->  ' + str(mySqrt(test_iter)))

# print(generate_list_of_squares())
