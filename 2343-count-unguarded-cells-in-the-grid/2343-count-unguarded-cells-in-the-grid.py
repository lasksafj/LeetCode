class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        A = [[0]*n for _ in range(m)]
        def f(guards, walls, m,n, t):
            mat = [[0]*n for _ in range(m)]
            for a,b in guards:
                mat[a][b] = 1
            for a,b in walls:
                mat[a][b] = -1
            for i in range(m):
                g = 0
                for j in range(n):
                    if mat[i][j] != 0:
                        g = mat[i][j]
                    a,b = (i,j) if t else (j,i)
                    A[a][b] = max(A[a][b], max(g, 0))
                g = 0
                for j in range(n-1,-1,-1):
                    if mat[i][j] != 0:
                        g = mat[i][j]
                    a,b = (i,j) if t else (j,i)
                    A[a][b] = max(A[a][b], max(g, 0))
        f(guards, walls, m, n, 1)
        guards = [[b,a] for a,b in guards]
        walls = [[b,a] for a,b in walls]
        f(guards, walls, n, m, 0)
        return m*n - sum(sum(r) for r in A) - len(walls)