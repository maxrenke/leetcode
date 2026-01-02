1from collections import defaultdict
2
3class Solution:
4    def repeatedNTimes(self, nums: List[int]) -> int:
5        buckets = defaultdict(list)
6        for num in nums:
7            buckets[num].append(num)
8
9        sorted_buckets = sorted(buckets.items(), key=lambda kv: len(kv[1]), reverse=True) # Step 
10        return sorted_buckets[0][0]