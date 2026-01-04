1from typing import List
2
3class Solution:
4    def sumFourDivisors(self, nums: List[int]) -> int:
5        def factor(n: int):
6            """Return prime factorization of n as dict {prime: exponent}."""
7            f = {}
8            d = 2
9            while d * d <= n:
10                while n % d == 0:
11                    f[d] = f.get(d, 0) + 1
12                    n //= d
13                d += 1 if d == 2 else 2  # after 2, check only odd numbers
14            if n > 1:
15                f[n] = f.get(n, 0) + 1
16            return f
17
18        total = 0
19
20        for n in nums:
21            if n < 6:
22                # smallest number with 4 divisors is 6 (1,2,3,6)
23                continue
24
25            f = factor(n)
26            if len(f) == 1:
27                # Possible form: p^e
28                (p, e), = f.items()
29                if e == 3:
30                    # n = p^3 → divisors: 1, p, p^2, p^3
31                    total += 1 + p + p * p + n
32            elif len(f) == 2:
33                # Possible form: p^1 * q^1
34                exps = list(f.values())
35                if exps[0] == 1 and exps[1] == 1:
36                    # n = p * q with p, q prime, distinct
37                    p, q = f.keys()
38                    # Sum of divisors: (1 + p) * (1 + q) = 1 + p + q + pq
39                    total += (1 + p) * (1 + q)
40
41        return total
42