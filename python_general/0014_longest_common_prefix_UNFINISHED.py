#!/usr/bin/python3
# Tim H 2023
# UNFINISHED
# https://leetcode.com/problems/longest-common-prefix/description/
"""docstring"""

class Solution:
    """docstring"""

    def longestCommonPrefix(self, strs: list[str]) -> str:
        """docstring"""
        res = '_'
        # sort the keys by length and then alphabetically
        # hopefully it will speed up the process of finding mismatches
        strs.sort()
        strs.sort(key=len)
        shortest_string = strs[0]
        print(strs)
        
        # exit early condition - if the shortest string is empty
        if len(shortest_string) == 0:
            return ""
        
        # early exit condition - if there's only 1 string to compare,
        # just return the whole thing
        if len(strs) == 1:
            return strs[0]

        # there are at least 2 strings to compare
        for outer_iter, outer_char in enumerate(shortest_string):
            inner_iter = 1
            for inner_char in strs[outer_iter]
            
            #for charY in strs[inner_iter]:
            charY = strs[inner_iter][]:
            print(charX + " " + charY)
            if charX != charY:
                return res
            inner_iter += 1
            res = res.append(charX)
        return res


###############################################################################
#       MAIN
###############################################################################

sol = Solution()

tests = [["flower", "flow", "flight"],
         ["dog", "racecar", "car"]]

for iter in tests:
    print(sol.longestCommonPrefix(iter))
