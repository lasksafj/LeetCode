class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        M,N = len(grid),len(grid[0])
        @cache
        def dfs(r,c1,c2):
            if r == M:
                return 0
            res = 0
            for nc1 in range(c1-1,c1+2):
                if nc1 < 0 or nc1 == N:
                    continue
                for nc2 in range(c2-1,c2+2):
                    if nc2 < 0 or nc2 == N:
                        continue
                    res = max(res, dfs(r+1,nc1,nc2))
            return res + grid[r][c1] + (grid[r][c2] if c1 != c2 else 0)
        return dfs(0,0,N-1)