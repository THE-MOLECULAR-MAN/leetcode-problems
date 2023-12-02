#!/usr/bin/python3
# Tim H 2023
# https://leetcode.com/problems/remove-vowels-from-a-string/
# Runtime:
# Memory:
""" module docstring """

import re


class Solution:
    """docstring"""
    def removeVowels(self, s: str) -> str:
        """docstring"""
        return re.sub(r"[a,e,i,o,u]", "", s)
