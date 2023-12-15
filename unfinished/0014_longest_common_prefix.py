#!/usr/bin/python3
# Tim H 2023
# UNFINISHED
# https://leetcode.com/problems/longest-common-prefix/description/
# Runtime: beats	%
# Memory:  beats	%
"""docstring"""


class Solution:
    """docstring"""

    def longestCommonPrefix(self, strs: list[str]) -> str:
        """docstring"""
        try:
            shortest_string = min(strs, key=len)
            print('shortest_string = ' + str(shortest_string))

            # iterate through each characer in the shorest string
            outer_iter = 0
            res = ''

            # prob should sort them by ascending length, or at least
            # put the shorest one first?

            while outer_iter < len(shortest_string):
                inner_iter = 1
                next_char = strs[outer_iter][inner_iter]

                while inner_iter < len(strs):

                    if strs[outer_iter][inner_iter] != next_char:
                        if inner_iter == 1:
                            return ""
                        return strs[0][0:outer_iter - 2]
                    inner_iter += 1
                res = res.append(next_char)
                outer_iter += 1
        except IndexError:
            # gotta fix something here. If the first string is shorter
            return res
        return True


###############################################################################
#       MAIN
###############################################################################

sol = Solution()

tests = [["flower", "flow", "flight"],
         ["dog", "racecar", "car"]]

for iter in tests:
    print(str(iter) + ' -->  ' + str(sol.longestCommonPrefix(iter)))
