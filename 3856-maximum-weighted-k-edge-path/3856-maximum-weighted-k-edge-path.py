class Solution:
    def maxWeight(self, n: int, edges: List[List[int]], k: int, t: int) -> int:
        dp = [{0} for _ in range(n)]
        for _ in range(k):
            ndp = [set() for _ in range(n)]
            for a,b,w in edges:
                for s in dp[a]:
                    if s+w < t:
                        ndp[b].add(s+w)
            dp = ndp
        res = -1
        for i in range(n):
            for s in dp[i]:
                res = max(res, s)
        return res