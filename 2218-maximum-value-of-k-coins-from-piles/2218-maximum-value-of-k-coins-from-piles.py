class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        @cache
        def dfs(i,k):
            if k == 0:
                return 0
            if i == len(piles):
                return 0
            s = 0
            res = dfs(i+1, k)
            for j in range(min(k,len(piles[i]))):
                s += piles[i][j]
                res = max(res, dfs(i+1, k-j-1) + s)
            return res
        return dfs(0,k)