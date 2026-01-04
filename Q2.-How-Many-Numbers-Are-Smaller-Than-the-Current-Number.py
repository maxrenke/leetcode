1class Solution:
2    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
3        # Sort a copy of nums
4        sorted_nums = sorted(nums)
5
6        # Map each number to the first index where it appears
7        first_index = {}
8        for i, val in enumerate(sorted_nums):
9            if val not in first_index:
10                first_index[val] = i
11
12        # Build and return the answer array
13        return [first_index[x] for x in nums]
14