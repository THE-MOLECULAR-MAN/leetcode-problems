#!/usr/bin/python3
# Tim H 2023
# https://leetcode.com/problems/find-words-containing-character/description/
# Runtime: beats	%
# Memory:  beats	%
"""docstring"""


class Solution:
    """docstring"""

    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        """docstring"""
        ans = []
        i = 0
        for i, word in enumerate(words):
            if x in word:
                ans.append(i)
        return ans
