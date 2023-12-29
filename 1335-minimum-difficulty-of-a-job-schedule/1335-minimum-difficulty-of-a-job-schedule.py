class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        @cache
        def dfs(i,ma,d):
            if i == len(jobDifficulty):
                return ma if d == 0 else inf
            if d < 0:
                return inf
            a = dfs(i+1,jobDifficulty[i],d-1) + ma
            b = dfs(i+1,max(ma, jobDifficulty[i]),d)
            return min(a,b)
        res = dfs(0,0,d) 
        return res if res < inf else -1