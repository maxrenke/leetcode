1from typing import List
2
3class Solution:
4    def longestBalanced(self, nums: List[int]) -> int:
5        max_len = 0
6        n = len(nums)
7        
8        for i in range(n):
9            evens = set()
10            odds = set()
11            
12            for j in range(i, n):
13                num = nums[j]
14                if num % 2 == 0:
15                    evens.add(num)
16                else:
17                    odds.add(num)
18                
19                if len(evens) == len(odds):
20                    current_len = j - i + 1
21                    if current_len > max_len:
22                        max_len = current_len
23        
24        return max_len
25