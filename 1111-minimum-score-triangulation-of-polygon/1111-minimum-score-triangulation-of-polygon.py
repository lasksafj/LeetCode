class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        @cache
        def dfs(l,r):
            if r-l+1 < 3:
                return 0
            if r-l+1 == 3:
                return prod(values[l:r+1])
            res = inf
            for k in range(l+1, r):
                res = min(res, dfs(l,k) + dfs(k,r) + values[l]*values[r]*values[k])
            return res
        return dfs(0, len(values)-1)