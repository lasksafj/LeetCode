class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        N = len(fruits)
        res = 0
        for i in range(N):
            res += fruits[i][i]
            fruits[i][i] = 0
        @cache
        def dfs1(i, j):
            if j == N or j <= i:
                return -inf
            if i == N:
                return 0
            res = 0
            for nj in [j-1,j,j+1]:
                res = max(res, dfs1(i+1, nj))
            return res + fruits[i][j]
        @cache
        def dfs2(i,j):
            if i == N or i <= j:
                return -inf
            if j == N:
                return 0
            res = 0
            for ni in [i-1,i,i+1]:
                res = max(res, dfs2(ni, j+1))
            return res + fruits[i][j]
        
        return res + dfs1(0,N-1) + dfs2(N-1,0)