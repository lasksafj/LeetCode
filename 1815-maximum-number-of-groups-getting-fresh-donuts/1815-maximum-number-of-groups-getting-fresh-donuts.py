class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        freq = [0]*batchSize
        for g in groups:
            freq[g % batchSize] += 1
        
        @cache
        def dfs(freq, r):
            res = 0
            ok = False
            for f in freq:
                if f > 0:
                    ok = True
            if ok:
                for i,f in enumerate(freq):
                    if f > 0:
                        A = freq[:i] + (f-1,) + freq[i+1:]
                        res = max(res, dfs(A, (r+i) % batchSize))
                if r == 0:
                    res += 1
            return res
        return dfs(tuple(freq), 0)