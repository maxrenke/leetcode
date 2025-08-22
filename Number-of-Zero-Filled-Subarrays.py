class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        total = 0
        streak = 0

        for n in nums:
            if n == 0:
                streak = streak + 1
                total = total + streak
            else:
                streak = 0 #reset
        
        return total