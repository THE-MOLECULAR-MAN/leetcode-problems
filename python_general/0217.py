from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return Counter(nums).most_common(1)[0][1] > 1
