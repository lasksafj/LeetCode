class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        s = [0]*(n+1)
        res = 0
        for i in range(n,n//2,-1):
            s[i] = cost[i-1]
        for i in range(n//2, 0, -1):
            s[i] = max(s[i*2], s[i*2+1]) + cost[i-1]
            res += abs(s[i*2] - s[i*2+1])
        return res