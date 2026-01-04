1class Solution:
2    def buildArray(self, target: List[int], n: int) -> List[str]:
3        ops = []
4        t = 0  # index in target
5
6        for num in range(1, n + 1):
7            if t == len(target):
8                break
9
10            ops.append("Push")
11
12            if num == target[t]:
13                t += 1
14            else:
15                ops.append("Pop")
16
17        return ops
18