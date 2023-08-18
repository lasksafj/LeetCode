class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        deg = [0]*n
        s = set()
        for a,b in roads:
            deg[a] += 1
            deg[b] += 1
            s.add((a,b))
        res = 0
        for i in range(n):
            for j in range(i+1, n):
                res = max(res, deg[i] + deg[j] - ((i,j) in s or (j,i) in s))
        return res