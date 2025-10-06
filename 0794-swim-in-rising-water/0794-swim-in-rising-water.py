class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        p = list(range(N**2))
        size = [1]*(N**2)
        def root(u):
            while u != p[u]:
                p[u] = p[p[u]]
                u = p[u]
            return u
        def union(u,v):
            u,v = root(u),root(v)
            if u == v: return
            if size[u] < size[v]:
                u,v = v,u
            p[v] = u
            size[u] += size[v]
        vis = [[False]*N for _ in range(N)]
        A = sorted([[i,j] for i in range(N) for j in range(N)], key=lambda e:grid[e[0]][e[1]])
        for i,j in A:
            vis[i][j] = True
            for ni,nj in (i+1,j),(i-1,j),(i,j-1),(i,j+1):
                if 0<=ni<N and 0<=nj<N and vis[ni][nj]:
                    union(i*N+j, ni*N+nj)
            if root(0) == root(N**2-1):
                return grid[i][j]
        return -1