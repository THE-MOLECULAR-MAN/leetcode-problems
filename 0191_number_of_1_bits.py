import operator as op


class Solution:
    def hammingWeight(self, n: int) -> int:
        return op.countOf(bin(n), "1")
