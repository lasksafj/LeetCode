class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        dp = [[[0]*(minProfit+1) for _ in range(n+1)] for _ in range(len(profit)+1)]
        dp[0][0][0] = 1
        for i in range(len(profit)):
            for p in range(n+1):
                for m in range(minProfit+1):
                    dp[i+1][p][m] += dp[i][p][m]
                    if p-group[i] >= 0:
                        dp[i+1][p][min(minProfit,m+profit[i])] += dp[i][p-group[i]][m]
                    
        res = 0
        for p in range(n+1):
            res += dp[-1][p][minProfit]
        return res % 1000000007