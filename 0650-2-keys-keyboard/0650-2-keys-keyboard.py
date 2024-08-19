class Solution:
    def minSteps(self, n: int) -> int:
        @cache
        def dfs(i,k):
            if i > n:
                return inf
            if i == n:
                return 0
            res = inf
            if k < i:
                res = dfs(i,i)
            if k > 0:
                res = min(res, dfs(i+k,k))
            return res+1
        return dfs(1,0)