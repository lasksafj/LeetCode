class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
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
            j = i+1
            dfs(j, path + [candidates[i]], s + candidates[i])
            while j < len(candidates) and candidates[i] == candidates[j]:
                j += 1
            dfs(j, path, s)
                
        dfs(0, [], 0)
        return res