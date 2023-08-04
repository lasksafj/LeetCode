class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        M,N = len(grid),len(grid[0])
        @cache
        def dfs(i,j,k):
            if 0 <= i < M and 0 <= j < N:
                a = 1 if grid[i][j] == '(' else -1
                if k+a < 0:
                    return False
                if i == M-1 and j == N-1 and k+a == 0:
                    return True
                return dfs(i+1,j, k + a) or dfs(i,j+1, k + a)
            return False
        return dfs(0,0,0)