class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        # dp[i,k]: min cost to to pain in k (time + no_paid) for [:i]

        N = len(cost)
        dp = [inf]*(N+1)
        dp[0] = 0
        for i in range(N):
            ndp = dp[:]
            for k in range(N+1):
                ndp[k] = min(ndp[k], dp[max(0, k-time[i]-1)] + cost[i])
            dp = ndp
        return dp[-1]