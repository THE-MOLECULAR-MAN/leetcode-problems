#!/usr/bin/python3
# Tim H 2023
# https://leetcode.com/problems/palindrome-number/description/
# Runtime: beats	%
# Memory:  beats	%
"""docstring"""


def isPalindrome(x: str) -> bool:
    """docstring"""
    # if x < 0:
    #    return False

    x_str = x
    leng = len(x_str)

    # working for even numbered strings
    # odd is wrong, too long

    if leng <= 1:
        return True
    if leng == 2:
        return x_str[0] == x_str[1]
    if leng == 3:
        return x_str[0] == x_str[2]

    # code up to here is solid

    if leng % 2 == 0:  # even
        end_of_left_str = (leng - 1) // 2
        start_of_right_str = end_of_left_str + 1
        left_side = x_str[0:end_of_left_str+1]
        right_side = x_str[leng-1:start_of_right_str-1:-1]
    else:   # odd
        end_of_left_str = ((leng - 1) // 2) - 1
        start_of_right_str = end_of_left_str + 2
        left_side = x_str[0:end_of_left_str+1]
        right_side = x_str[leng-1:start_of_right_str-1:-1]

    print("original= ", x, "  left =", left_side, "  right =", right_side)
    return left_side == right_side

###############################################################################
#       MAIN
###############################################################################


# assert isPalindrome("012345") == False
assert isPalindrome("0123456") is False
# assert isPalindrome("888888") == True
# assert isPalindrome("88888")  == True
