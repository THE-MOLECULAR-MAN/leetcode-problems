# https://leetcode.com/problems/shortest-word-distance/description/
class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        # simple, exit early case:
        if len(wordsDict) == 2: return 1

        # build 2 lists that have all the indices of both words
        word1_indexes = [i for i, n in enumerate(wordsDict) if n == word1]
        word2_indexes = [i for i, n in enumerate(wordsDict) if n == word2]

        # assume worst case scenario first, that they're at opposite ends
        res = len(wordsDict)

        # loop through both lists - O(n^2) unfortunately
        for w1_val in word1_indexes:
            for w2_val in word2_indexes:
                res = min(res,abs(w1_val-w2_val))
        return res
