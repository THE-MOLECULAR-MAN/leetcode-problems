#!/usr/bin/python3
# Tim H 2023
# https://leetcode.com/problems/pascals-triangle/
# Runtime:  beats 67%
# Memory:   beats 52%
# TODO: preallocate entire list structure ahead of time instead of appending
# then can just 2 nested loops to access via indexes
"""docstring"""

# def get_last_row(l):
#     """docstring"""
#     return l[-1]


def create_next_row(r):
    """docstring"""
    next_row = [1] * (len(r) + 1)
    i = 1
    while i <= len(r)-1:
        next_row[i] = r[i-1] + r[i]
        i += 1
    return next_row


class Solution:
    """docstring"""

    def generate(self, numRows: int) -> list[list[int]]:
        """docstring"""
        res = [[1]]
        i = 1
        while i < numRows:
            # nextr = get_last_row(res)
            # nextr = res[-1]
            res.append(create_next_row(res[-1]))
            i += 1
        return res


print(Solution().generate(5))
