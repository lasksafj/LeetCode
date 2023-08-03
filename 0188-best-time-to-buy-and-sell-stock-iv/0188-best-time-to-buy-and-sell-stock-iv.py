class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        @cache
        def dfs(i, k, buy):
            if i == len(prices):
                return 0
            a = dfs(i+1,k, buy)
            if buy and k > 0:
                b = dfs(i+1, k-1, buy^1) - prices[i]
            elif not buy:
                b = dfs(i+1, k, buy^1) + prices[i]
            else:
                b = 0
            return max(a,b)
        return dfs(0,k,1)