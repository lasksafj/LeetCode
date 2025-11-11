class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        @cache
        def dfs(i, m, n):
            if i == len(strs):
                return 0
            mp = Counter(strs[i])
            res = dfs(i+1, m, n)
            if mp['0'] <= m and mp['1'] <= n:
                res = max(res, dfs(i+1, m-mp['0'], n-mp['1']) + 1)
            return res
        return dfs(0,m,n)