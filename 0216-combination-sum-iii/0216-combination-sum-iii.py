class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def dfs(d, t, path):
            if len(path) == k:
                if t == n:
                    res.append(path[:])
                return
            if t > n or d > 9:
                return
            dfs(d+1, t+d, path + [d])
            dfs(d+1, t, path)
        dfs(1, 0, [])
        return res