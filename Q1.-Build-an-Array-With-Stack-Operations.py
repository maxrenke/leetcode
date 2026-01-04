1class Solution:
2    def buildArray(self, target: List[int], n: int) -> List[str]:
3        ops = []
4        prev = 0
5
6        for x in target:
7            # Push+Pop for all numbers between prev and x
8            for _ in range(x - prev - 1):
9                ops.append("Push")
10                ops.append("Pop")
11
12            ops.append("Push")
13            prev = x
14
15        return ops
16