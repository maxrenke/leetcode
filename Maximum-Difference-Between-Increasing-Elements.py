class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max = -1 #if no such i,j exist return -1
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if i > j:
                    continue
                diff = nums[j] - nums[i]
                if diff > 0 and diff > max:
                    max = diff
        return max