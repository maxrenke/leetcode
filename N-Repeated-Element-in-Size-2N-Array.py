1from collections import defaultdict
2
3class Solution:
4    def repeatedNTimes(self, nums: List[int]) -> int:
5        count = collections.Counter(nums)
6        for k in count:
7            if count[k] > 1:
8                return k