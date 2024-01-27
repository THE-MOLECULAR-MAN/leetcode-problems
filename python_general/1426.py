class Solution:
    def countElements(self, arr: List[int]) -> int:
        # Constant Memory O(1)
        # O(n^2) compute
        
        if len(arr) == 1: return 0

        output = 0

        for val in arr:
            if val + 1 in arr: output += 1

        return output
        # could prob use Counters too since the order doesn't matter