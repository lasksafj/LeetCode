from sortedcontainers import SortedList

class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        if k == 0:
            return max(vals)
        s = [SortedList() for _ in range(len(vals))]
        for a,b in edges:
            if vals[b] > 0:
                s[a].add(vals[b])
            if vals[a] > 0:
                s[b].add(vals[a])
        return max(sum(e[-k:])+vals[i] for i,e in enumerate(s))