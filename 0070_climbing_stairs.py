#!/usr/bin/python3
# Tim H 2023
# https://leetcode.com/problems/climbing-stairs/description/
# Runtime:
# Memory:
""" module docstring """


class Solution:
    """docstring"""
    def climbStairs(self, n: int) -> int:
        """docstring"""
        # there's def a O(n^2) solution that's slow af, prob using recursion
        # but is there a math formula to determine this?
        if n < 3:
            return n


###############################################################################
#       MAIN
###############################################################################
sol = Solution()

tests = [1, 2, 3, 4, 5, 16, 32, 45]

for test_iter in tests:
    print(str(test_iter) + ' -->  ' + str(sol.testname(test_iter)))
