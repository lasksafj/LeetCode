class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        @cache
        def dfs(i):
            if i == len(strs[0]):
                return 0
            res = 1
            for j in range(i+1, len(strs[0])):
                if all(strs[r][i] <= strs[r][j] for r in range(len(strs))):
                    res = max(res, dfs(j) + 1)
            return res
        # print(dfs(1))
        return len(strs[0]) - max(dfs(i) for i in range(len(strs[0])))