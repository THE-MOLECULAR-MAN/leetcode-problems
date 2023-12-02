#!/usr/bin/python3
# Tim H 2023
# https://leetcode.com/problems/defanging-an-ip-address/description/
# Runtime:
# Memory:
"""docstring"""


class Solution:
    """docstring"""
    def defangIPaddr(self, address: str) -> str:
        """docstring"""
        return address.replace('.', '[.]', 3)
