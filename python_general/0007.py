import sys

class Solution:
    def reverse(self, x: int) -> int:
        # prob other ways with // 10 and modular division
        MIN_VAL = - (2 ** 31)
        MAX_VAL = (2 ** 31) - 1
        
        s = str(abs(x))
        s = s[::-1]

        if x < 0:
            s = '-' + s

        res = int(s)
        
        if res > MAX_VAL or res < MIN_VAL:
            return 0

        return res