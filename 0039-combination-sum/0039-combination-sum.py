class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def dfs(i, path, s):
            if s > target:
                return
            if s == target:
                res.append(path[:])
                return
            if i == len(candidates):
                return
            dfs(i, path + [candidates[i]], s + candidates[i])
            dfs(i+1, path, s)
                
        dfs(0, [], 0)
        return res