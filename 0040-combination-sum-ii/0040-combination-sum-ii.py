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
            while i < len(candidates):
                dfs(i+1, path + [candidates[i]], s + candidates[i])
                j = i+1
                while j < len(candidates) and candidates[i] == candidates[j]:
                    j += 1
                i = j
                
        dfs(0, [], 0)
        return res