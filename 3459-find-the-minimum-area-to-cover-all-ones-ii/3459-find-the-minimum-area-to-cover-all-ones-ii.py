class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        def F(grid):
            @cache
            def area(i1,i2,j1,j2):
                a,c = inf,inf
                b,d = -inf,-inf
                for i in range(i1,i2+1):
                    for j in range(j1,j2+1):
                        if grid[i][j]:
                            a = min(a, j)
                            b = max(b, j)
                            c = min(c, i)
                            d = max(d, i)
                if a == inf: return 0
                return (b-a+1) * (d-c+1)
            m = len(grid)
            n = len(grid[0])
            res = inf
            for i in range(m-1):
                for j in range(n-1):
                    res = min(
                        res, 
                        area(0,m-1,0,j) + area(0,i,j+1,n-1) + area(i+1,m-1,j+1,n-1),
                        area(0,i,0,j) + area(i+1,m-1,0,j) + area(0,m-1,j+1,n-1)
                    )
            for j1 in range(n-2):
                for j2 in range(j1+1, n-1):
                    res = min(
                        res, 
                        area(0,m-1,0,j1) + area(0,m-1,j1+1,j2) + area(0,m-1,j2+1,n-1)
                    )
            return res
        return min(F(grid), F(list(zip(*grid))))