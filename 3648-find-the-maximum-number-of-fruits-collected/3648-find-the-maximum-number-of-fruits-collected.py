class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        N = len(fruits)
        res = 0
        for i in range(N):
            res += fruits[i][i]
            fruits[i][i] = 0
        @cache
        def dfs1(i, j):
            if i == N-1:
                return 0 if j == N-1 else -inf
            res = -1
            for nj in [j-1,j,j+1]:
                if (N+1)//2 <= nj < N:
                    res = max(res, dfs1(i+1, nj))
            if res == -1: return -inf
            return res + fruits[i][j]
        @cache
        def dfs2(i,j):
            if j == N-1:
                return 0 if i == N-1 else -inf
            res = -1
            for ni in [i-1,i,i+1]:
                if (N+1)//2 <= ni < N:
                    res = max(res, dfs2(ni, j+1))
            if res == -1: return -inf
            return res + fruits[i][j]
        
        return res + dfs1(0,N-1) + dfs2(N-1,0)