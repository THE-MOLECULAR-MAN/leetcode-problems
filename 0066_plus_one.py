#!/usr/bin/python3
# Tim H 2023
# https://leetcode.com/problems/plus-one/description/description/
# Runtime:
# Memory:
"""docstring"""


def plusOne(digits: list[int]) -> list[int]:
    """docstring"""
    if digits[-1] < 9:  # don't need to carry a one, simplest case
        digits[-1] = digits[-1] + 1
        return digits

    # do need to carry at least one once
    digits[-1] = 0      # set the last digit to zero
    i = len(digits) - 2     # start a loop at the next to last number
    while i >= 0:
        if digits[i] < 9:   # can stop carrying the number
            digits[i] += 1  # increment the current digit, no need to carry
            return digits
        # do need to carry
        digits[i] = 0   # set the current number as 0
        if i == 0:      # the leading digit is a 9 and need to
            digits.insert(0, 1)
            return digits
        i -= 1
    digits.insert(0, 1)
    return digits


###############################################################################
#       MAIN
###############################################################################

tests = [[0],
         [1],
         [9],
         [9, 9, 9],
         [1, 0, 9],
         [1, 9, 9],
         [9, 9, 9],
         [9, 0, 0]
         ]

for test_iter in tests:
    print(str(test_iter) + ' -->  ' + str(plusOne(test_iter)))
