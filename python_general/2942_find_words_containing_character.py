#!/usr/bin/python3
# Tim H 2023
# https://leetcode.com/problems/find-words-containing-character/description/
# Runtime: beats	%
# Memory:  beats	%
"""docstring"""


class Solution:
    """docstring"""

    def findWordsContaining(self, words: list[str], x: str) -> list[int]:
        """docstring"""
        ans = []
        i = 0
        for i, word in enumerate(words):
            if x in word:
                ans.append(i)
        return ans
