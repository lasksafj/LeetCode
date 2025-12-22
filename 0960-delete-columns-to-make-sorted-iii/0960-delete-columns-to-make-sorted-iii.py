class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        def lte(a,b):
            return (a == -1) or all(strs[i][a] <= strs[i][b] for i in range(len(strs)))
        @cache
        def dfs(i, j):
            if i == len(strs[0]):
                return 0
            res = dfs(i+1, j) + 1
            if not lte(j, i):
                return res
            return min(dfs(i+1, i), res)
        return dfs(0, -1)