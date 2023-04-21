class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        @cache
        def dfs(i, minProfit, pp):
            if pp > n:
                return 0
            if i == len(profit):
                if pp <= n and minProfit == 0:
                    return 1
                return 0
            return (dfs(i+1, max(0,minProfit-profit[i]), pp+group[i]) % 1000000007)\
                + (dfs(i+1, minProfit, pp) % 1000000007) % 1000000007
        return dfs(0,minProfit,0) % 1000000007