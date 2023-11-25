class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        @cache
        def dfs(i):
            if i > len(prices):
                return 0
            res = inf
            for j in range(i+1,i+i+2):
                res = min(res, dfs(j))
            return res + prices[i-1]
        return dfs(1)