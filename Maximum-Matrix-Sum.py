1class Solution:
2    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
3        total_abs = 0
4        min_abs = float('inf')
5        neg_count = 0
6        
7        for row in matrix:
8            for x in row:
9                total_abs += abs(x)
10                min_abs = min(min_abs, abs(x))
11                if x < 0:
12                    neg_count += 1
13        
14        # If the number of negatives is even, all can be made positive
15        if neg_count % 2 == 0:
16            return total_abs
17        
18        # Otherwise, one smallest absolute value must remain negative
19        return total_abs - 2 * min_abs