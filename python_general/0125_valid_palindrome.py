#!/usr/bin/python3
# Tim H 2023
# https://leetcode.com/problems/valid-palindrome/
# Runtime: beats	97%
# Memory:  beats	13%
"""docstring"""

from re import sub


class Solution:
    """dummy docstring for leetcode class to meet pep8 style guide"""

    def simplify_string(self, s: str) -> str:
        """removes all non-alphanumeric characters from string and converts
        everything to lower case"""
        return sub("[^0-9a-zA-Z]+", "", s).lower()

    def is_even(self, num: int) -> bool:
        """returns boolean if num is an even number """
        return bool(num % 2 == 0)

    def get_mirrors(self, s: str) -> (str, str):
        """returns the two strings that should be compared to test if s
        is a palindrome."""
        L = len(s)
        if self.is_even(L):
            end_of_left = (L - 1) // 2
            start_of_right = end_of_left + 1
        else:
            end_of_left = ((L - 1) // 2) - 1
            start_of_right = end_of_left + 2

        return s[0:end_of_left+1], s[L-1:start_of_right-1:-1]

    def isPalindrome(self, s: str) -> bool:
        """returns boolean if s is a palindrome"""

        # unique cases for early exit
        # commented out since the problem says that s.length is at least 1
        # if s is None:
        #    return True

        # strip out the non-alphanumeric characters
        s = self.simplify_string(s)

        # another early exit
        # split this out b/c some test cases might be a long list of
        # non-alphanumerics with only 1 or fewer valid chars to test.
        # That would be slow
        if len(s) <= 1:
            return True

        # fetch the two strings to test if they match
        # uses extra memory, but is pretty fast
        leftside, rightside = self.get_mirrors(s)
        # print(s + " " + leftside + " " + rightside)
        return leftside == rightside
