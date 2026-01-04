1class Solution:
2    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
3        # Mark seen numbers by negating the value at their index
4        for x in nums:
5            idx = abs(x) - 1
6            if nums[idx] > 0:
7                nums[idx] *= -1
8
9        # Collect indices that remain positive → missing numbers
10        result = []
11        for i in range(len(nums)):
12            if nums[i] > 0:
13                result.append(i + 1)
14
15        return result
16