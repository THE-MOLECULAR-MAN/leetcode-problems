#!/usr/bin/python3
# Tim H 2023
# https://leetcode.com/problems/happy-number/description/
# Runtime: beats	75-95%
# Memory:  beats	10%
"""docstring"""

class Solution:
    """docstring"""
    def __init__(self):
        """Constructor that initializes an empty history
        using a private variable to save memory,
        instead of passing the history through
        recursive methods that would likely use more memory."""
        self.history = []
    

    def isHappy(self, n: int) -> bool:
        """docstring"""
        try:
            # base case, finally got a 1, can return True
            if n == 1:
                return True
            
            # check if this number has been seen before. If so, then we're
            # in a loop that indicates that it will never converge to 1
            # so it's time to return False- this isn't a happy number
            if n in self.history[:-1]:
                return False
            
            # compute the next number
            next_number = sum(int(x) * int(x) for x in str(n))
            
            # add it to the history
            self.history.append(next_number)
            
            # recursion case: pass along the history
            return self.isHappy(next_number)
            
        except RecursionError:
            return False
