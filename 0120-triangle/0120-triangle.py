class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        @cache
        def dfs(r, i):
            if r == len(triangle):
                return 0
            if i == len(triangle[r]):
                return inf
            return min(dfs(r+1, i), dfs(r+1, i+1)) + triangle[r][i]
        return dfs(0, 0)