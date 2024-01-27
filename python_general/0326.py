from math import log

class Solution:
    def __init__(self):
        self.log_base = 3

    def isPowerOfArbitrary(self, n: int) -> bool:
        if n == 1 or n == self.log_base:
            return True

        if n < 1 or (n % self.log_base > 0):
            return False

        return self.isPowerOfArbitrary(n / self.log_base)

    def isPowerOfThree(self, n: int) -> bool:       
        return self.isPowerOfArbitrary(n)
