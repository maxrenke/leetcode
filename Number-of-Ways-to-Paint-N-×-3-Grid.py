1class Solution:
2    def numOfWays(self, n: int) -> int:
3        MOD = 10**9 + 7
4        
5        a = 6  # Type A
6        b = 6  # Type B
7        
8        for _ in range(1, n):
9            a, b = (2*a + 2*b) % MOD, (2*a + 3*b) % MOD
10        
11        return (a + b) % MOD
12