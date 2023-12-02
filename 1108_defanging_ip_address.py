#!/usr/bin/python3
# Tim H 2023
# https://leetcode.com/problems/defanging-an-ip-address/description/
# Runtime:
# Memory:
""" module docstring """


class Solution:
    """doc string"""
    def defangIPaddr(self, address: str) -> str:
        """doc string"""
        return address.replace('.', '[.]', 3)
