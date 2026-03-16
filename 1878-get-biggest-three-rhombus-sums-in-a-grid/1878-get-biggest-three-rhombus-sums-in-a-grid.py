class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        M,N = len(grid),len(grid[0])
        # d: dir -1: left, 1: right
        # l: length
        @cache
        def dp(i,j,d,l):
            if not (0<=i<M and 0<=j<N):
                return -inf
            if l == 1:
                return grid[i][j]
            return dp(i+1, j+d, d, l-1) + grid[i][j]
        def max3(res, x):
            if x in res: return res
            a,b,c = res
            if x > a:
                a,b,c = x,a,b
            elif x > b:
                b,c = x,b
            elif x > c:
                c = x
            return [a,b,c]
        res = [0,0,0]
        for i in range(M):
            for j in range(N):
                res = max3(res, grid[i][j])
        for l in range(2, min(M,N)//2 + 2):
            for i in range(M):
                for j in range(N):
                    il,jl = i+l-1, j-(l-1)
                    ir,jr = i+l-1, j+l-1
                    ib,jb = i+2*(l-1), j
                    if ib < M and jl >= 0 and jr < N:
                        res = max3(res, dp(i,j,-1,l) + dp(i,j,1,l) + dp(il,jl,1,l) + dp(ir,jr,-1,l)
 - grid[i][j] - grid[il][jl] - grid[ir][jr] - grid[ib][jb]  )
        return [r for r in res if r]