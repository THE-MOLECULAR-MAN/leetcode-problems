#!/usr/bin/python3
# Tim H 2023
# https://leetcode.com/problems/palindrome-number/description/
# Runtime:
# Memory:
"""docstring"""

class Solution:
    """docstring"""
    def isPalindrome(self, x: int) -> bool:
        """docstring"""
        if x < 0:
            return False

        x_str = str(x)
        leng = len(x_str)

        if leng <= 1:
            return True
        elif leng == 2:
            return x_str[0] == x_str[1]
        elif leng == 3:
            return x_str[0] == x_str[2]

        if (leng % 2 == 0):  # even
            end_of_left_str = (leng - 1) // 2
            start_of_right_str = end_of_left_str + 1
            left_side = x_str[0:end_of_left_str+1]
            right_side = x_str[leng-1:start_of_right_str-1:-1]
        else:   # odd
            end_of_left_str = ((leng - 1) // 2) - 1
            start_of_right_str = end_of_left_str + 2
            left_side = x_str[0:end_of_left_str+1]
            right_side = x_str[leng-1:start_of_right_str-1:-1]

        return left_side == right_side
