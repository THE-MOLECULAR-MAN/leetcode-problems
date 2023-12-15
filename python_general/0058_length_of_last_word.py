#!/usr/bin/python3
# Tim H 2023
# https://leetcode.com/problems/length-of-last-word/description/
# Runtime: beats	%
# Memory:  beats	%
"""docstring"""


class Solution:
    """docstring"""

    def lengthOfLastWord(self, s: str) -> int:
        """docstring"""
        s = s.strip()
        last_space_index = s.rfind(' ')
        if last_space_index < 0:
            return len(s)
        return len(s) - last_space_index - 1
