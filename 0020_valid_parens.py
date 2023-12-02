#!/usr/bin/python3
# Tim H 2023
# https://leetcode.com/problems/valid-parentheses/description/
# Runtime: 30 ms,    Beats 95.43% of users with Python3
# Memory:  16.38 MB, Beats 25.71% of users with Python3
# https://leetcode.com/problems/valid-parentheses/solutions/4345396/python3-high-speed-beats-95-of-runtime/
#
# Intuition
# * Use a stack to track which characters have been pushed and what should
#  be next to pop
# Approach
# * Each paren should have a matching counterpart, so it will immediately fail
# # if the length of s is not even
# * Create a dictionary that maps which characters align to a push and pop.
# #   It's easy to add support for new pairs of characters this way like < and >
# * Walk through the string, each time a pushable character is detected, push
# # it onto the stack. Each time a popable character is detected, see if it
# # matches the last one pushed. If they don't match - immediately return False
# # If they do match, keep going.
# * When you reach the end of the string and haven't encountered any issues,
# # return if the stack is empty. If the stack is empty, then return True.
# # Otherwise return false.
# * If a pop fails due to an exception, return False
# Complexity
# * Time complexity: O(n)O(n)O(n)
# * Space complexity: O(n)O(n)O(n)
"""docstring"""


class Solution:
    """docstring"""

    def isValid(self, s: str) -> bool:
        """docstring"""
        if len(s) < 2 or len(s) % 2 != 0:
            return False

        stack = []
        mapping = {"(": r')', "[": r']', "{": r'}'}

        i = 0
        try:
            while i < len(s):
                new_char = s[i]
                # check if in the keys (pushing onto stack)
                if new_char in mapping:
                    stack.append(new_char)  # push it
                elif mapping[stack.pop()] != new_char:
                    return False
                i += 1
        except IndexError:
            return False
        return len(stack) == 0


###############################################################################
#       MAIN
###############################################################################

sol = Solution()

tests = [r'()', r'()[]{}', r'(]', r')', "){"]

for test_iter in tests:
    print(str(test_iter) + ' -->  ' + str(sol.isValid(test_iter)))
