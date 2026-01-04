1class Solution:
2    def findErrorNums(self, nums: List[int]) -> List[int]:
3        dup = -1
4        missing = -1
5
6        # Find duplicate by marking visited numbers
7        for x in nums:
8            idx = abs(x) - 1
9            if nums[idx] < 0:
10                dup = abs(x)
11            else:
12                nums[idx] *= -1
13
14        # Find missing (index still positive)
15        for i in range(len(nums)):
16            if nums[i] > 0:
17                missing = i + 1
18                break
19
20        return [dup, missing]
21