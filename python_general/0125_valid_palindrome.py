#!/usr/bin/python3
# Tim H 2023
# https://leetcode.com/problems/valid-palindrome/
# high speed but high memory utilization approach
# Runtime: beats	97%     O(n)
# Memory:  beats	13%     O(n)

# Could be rewritten as iterative approach that doesn't use any extra memory
# but it'd prob be slower than comparing two strings
"""docstring"""

from re import sub


class Solution:
    """dummy docstring for leetcode class to meet pep8 style guide"""

    def simplify_string(self, s: str) -> str:
        """removes all non-alphanumeric characters from string and converts
        everything to lower case"""
        # I think using a compiled regex is a little faster than this?
        return sub("[^0-9a-zA-Z]+", "", s).lower()

    def is_even(self, num: int) -> bool:
        """returns boolean if num is an even number """
        # adding bool() for extra readability for newbies, but it is
        # not required
        return bool(num % 2 == 0)

    def get_mirrors(self, s: str) -> (str, str):
        """returns the two strings that should be compared to test if s
        is a palindrome."""
        L = len(s)
        if self.is_even(L):
            # the string has an even number of characters, so we don't need
            # to worry about ignoring a middle character
            end_of_left = (L - 1) // 2
            start_of_right = end_of_left + 1
        else:
            # string has an odd number of characters
            # the first string will go from 0 to 1 character before the middle
            # the second string will start just after the middle character
            end_of_left = ((L - 1) // 2) - 1
            start_of_right = end_of_left + 2

        # returns the first string forward, and the second string in reverse
        # using reverse indexes is a little faster than using functions like
        # reverse()
        return s[0:end_of_left+1], s[L-1:start_of_right-1:-1]

    def isPalindrome(self, s: str) -> bool:
        """returns boolean if s is a palindrome"""

        # unique cases for early exit
        # commented out since the problem says that s.length is at least 1
        # if s is None:
        #    return True

        # strip out the non-alphanumeric characters
        s = self.simplify_string(s)

        # Early exit for special cases:
        # Intentionally doing this test AFTER the simplify_string
        # b/c some test cases might be a long list of
        # non-alphanumerics with only 1 or fewer valid chars to test.
        if len(s) <= 1:
            return True

        # fetch the two strings to test if they match
        # uses extra memory, but is pretty fast
        leftside, rightside = self.get_mirrors(s)

        # leftover from debugging:
        # print(s + " " + leftside + " " + rightside)

        return leftside == rightside
