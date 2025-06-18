class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(0,len(nums)-2,3): # 3 at a time
            group = nums[i:i+3]
            if( group[2] - group[0] > k ):
                return []

            ans.append(group)
        return ans
