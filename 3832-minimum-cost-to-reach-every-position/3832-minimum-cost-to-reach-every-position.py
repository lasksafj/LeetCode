class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        N = len(cost)
        res = [0]*N
        res[0] = cost[0]
        mi = inf
        for i in range(1, N):
            res[i] = min(cost[i], res[i-1])
        return res