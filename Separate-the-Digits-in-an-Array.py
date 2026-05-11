1class Solution(object):
2    def separateDigits(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: List[int]
6        """
7        digits = []
8        for n in nums:
9            if n == 0:
10                digits.append(0)
11                continue
12            temp = []
13            while n > 0:
14                temp.append(n % 10)
15                n //= 10
16            for d in reversed(temp):
17                digits.append(d)
18        return digits