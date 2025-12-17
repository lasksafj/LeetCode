class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        N = len(prices)
        dp = [[[-inf]*3 for _ in range(k+1)] for _ in range(N)]
        def dfs(i,k,state):
            if i == len(prices):
                return 0 if state == 0 else -inf
            if dp[i][k][state] > -inf:
                return dp[i][k][state]
            res = dfs(i+1, k, state)
            if k:
                if state == 0:
                    res = max(res, dfs(i+1, k, 1) - prices[i])
                    res = max(res, dfs(i+1, k, 2) + prices[i])
                elif state == 1:
                    res = max(res, dfs(i+1, k-1, 0) + prices[i])
                else:
                    res = max(res, dfs(i+1, k-1, 0) - prices[i])
            dp[i][k][state] = res
            return res
        return dfs(0, k, 0)