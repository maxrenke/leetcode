1class Solution:
2    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
3        max_count = 0 
4        current = 0
5        for n in nums: 
6            if n == 1: 
7                current += 1 
8                max_count = max(max_count, current) 
9            else: 
10                current = 0 
11        return max_count