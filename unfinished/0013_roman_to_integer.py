#!/usr/bin/python3
# Tim H 2023
# UNFINISHED
# https://leetcode.com/problems/roman-to-integer/description/
# Problem: 0013
# Runtime: beats	%
# Memory:  beats	%
"""docstring"""


import numpy as np


def is_descending(r) -> bool:
    """docstring"""
    # print('sorted version: ', sorted(r))
    return r == sorted(r, reverse=True)


def get_subtraction_list(l):
    """docstring"""
    return 0


def find_next_change(l):
    """docstring"""
    # for i in l:
    # if
    return 0


def romanToInt(s: str):
    """docstring"""
    mapping = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    print('-------------------------')
    print('original: ', s)

    # if len(s) == 0:
    #     return 0
    # elif len(s) == 1:
    #     return mapping[s[0]]

    # while iter<len(s)-1:
    #     x=mapping[s[iter]]
    #     x_next=mapping[s[iter+1]]
    #     if x_next > x:
    #         # need to do subtraction

    # romans_as_array = [char for char in s]
    numerical_list = []
    for c in s:
        numerical_list.append(mapping[c])

    if is_descending(numerical_list):
        print('no logic needed, list is descending')
        return sum(numerical_list)

    print('gotta do some logic, it is ascending')

    return numerical_list

###############################################################################
#       MAIN
###############################################################################


print(romanToInt('I'))
print(romanToInt(''))
print(romanToInt('III'))
print(romanToInt('IV'))
print(romanToInt('VI'))
