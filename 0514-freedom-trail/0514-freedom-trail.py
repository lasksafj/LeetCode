class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        @cache
        def dfs(i, j):
            if i == len(key):
                return 0
            res = inf
            for k in range(len(ring)):
                if ring[k] == key[i]:
                    res = min(res, dfs(i+1, k) + min(abs(j-k), len(ring)-abs(j-k)))
            return res + 1
        return dfs(0, 0)