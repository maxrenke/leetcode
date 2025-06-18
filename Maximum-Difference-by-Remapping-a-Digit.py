class Solution:
    def minMaxDifference(self, num: int) -> int:
        used = set()
        min = 100000000
        max = 0
        for digit in str(num):
            used.add(digit)
        for d1 in used:
            for d2 in range(0,10):
                val = int(str(num).replace(str(d1),str(d2)))
                if val > max: max = val 
                if val < min: min = val

        return max - min