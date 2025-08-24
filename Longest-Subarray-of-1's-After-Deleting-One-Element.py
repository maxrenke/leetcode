class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeros_index = []
        for index, n in enumerate(nums):
            if n == 0:
                zeros_index.append(index)

        if( len(zeros_index) == 0 ):
            return len(nums) - 1

        max_length = 0
        left = 0
        for i, zero in enumerate(zeros_index):
            if i+1 >= len(zeros_index):
                right = len(nums)
            else:
                right = zeros_index[i+1]
            # left <> zero + zero <> right
            length = (zero - left) + (right - zero -1)
            max_length = max(length, max_length)
            left = zero + 1

        
        return max_length

