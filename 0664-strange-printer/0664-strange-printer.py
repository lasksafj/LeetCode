class Solution:
    def strangePrinter(self, s: str) -> int:
        @cache
        def dfs(i,j):
            if i == j:
                return 1
            res = 1 + dfs(i+1,j)
            for k in range(i+1,j+1):
                if s[i] == s[k]:
                    res = min(res, dfs(i+1,k) + (dfs(k+1,j) if k<j else 0))
            return res
        return dfs(0,len(s)-1)