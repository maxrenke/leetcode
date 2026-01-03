1class Solution:
2    def shuffle(self, nums: List[int], n: int) -> List[int]:
3        ans = [] 
4        for i in range(n): 
5            ans.append(nums[i]) 
6            ans.append(nums[i+n])
7        return ans
8