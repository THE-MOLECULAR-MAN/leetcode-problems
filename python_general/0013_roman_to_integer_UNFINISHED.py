#!/usr/bin/python3
# Tim H 2023
# UNFINISHED
# https://leetcode.com/problems/roman-to-integer/description/
"""docstring"""


# import numpy as np

class Solution:
    """docstring"""

    def __init__(self):
        self.sum = 0
        self.MAPPING = {'I': 1, 'V': 5, 'X': 10,
                        'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def romanToInt(self, s: str) -> int:
        """docstring"""

        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return self.MAPPING[s[0]]

        numerical_list = []
        for c in s:
            numerical_list.append(self.MAPPING[c])
        
        x = self.break_into_pieces(numerical_list)
        r = self.summarize_arrays(x)
        return self.sum
    
    def summarize_arrays(self,nums):
        """docstring"""
        for iter_array in nums:
            self.sum += self.summarize_single_number(iter_array)
            
    def summarize_single_number(self, n_list):
        """docstring"""
        first = n_list[0]
        last = n_list[-1]

        # if subtraction needs to take place:
        if last > first:
            return last - sum(n_list[0:-2])
        else:
            return sum(n_list)
        
    def break_into_pieces(self, nums):
        """docstring"""
        res = []
        inner = [0]
        for i in nums:
            # current number is increasing or the same, append into group
            if i >= inner[-1]:
                inner.append(i)

            # otherwise, a new string is starting
            else:
                res.append(inner)
                inner = [i]
        res.append(inner)
        return res

    def is_descending(self, r) -> bool:
        """docstring"""
        return r == sorted(r, reverse=True)


###############################################################################
#       MAIN
###############################################################################
sol = Solution()

test_inputs = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]

for iter_input in test_inputs:
    iter_output = sol.romanToInt(iter_input)
    print(f'input: {iter_input}   output: {iter_output}')
