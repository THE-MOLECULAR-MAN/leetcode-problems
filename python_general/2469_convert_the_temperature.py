#!/usr/bin/python3
# Tim H 2023
# https://leetcode.com/problems/convert-the-temperature/
# Runtime: beats	%
# Memory:  beats	%
"""docstring"""


class Solution:
    """docstring"""

    def convertTemperature(self, celsius: float) -> list[float]:
        """docstring"""
        return [celsius + 273.15, (celsius * 1.80) + 32.00]
