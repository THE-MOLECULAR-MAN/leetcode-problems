# from math import log2

class Solution:
    """Solution class required by leetcode"""
    def isPowerOfTwo(self, n: int) -> bool:
        """Method defined by LeetCode
        this method checks to see if the integer n is a power of two"""
        
        # # do some quick checks that are fast before doing the expensive calculation
        # # n needs to be at least 1 to return True
        # # n also must be even for n >= 3
        # # return early with False, don't bother computing the log2(n)
        # if n < 1 or (n >= 3 and n % 2) == 1: return False

        # # compute the log base 2 of n
        # # this is the bulk of the computational cost of this function
        # log2n = log2(n)

        # # if that value rounded down to the nearest integer
        # # is equal to itself then it's an integer
        # return int(log2n) == log2n
        return n and not (n & n - 1)


#   faster version using bitshifting
#   return n and not (n & n - 1)