class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        f = {}
        r = {}
        def find(u):
            if u not in f:
                f[u] = u
                r[u] = 0
            while f[u] != u:
                u = f[u]
            return u
        def union(u,v):
            u = find(u)
            v = find(v)
            if u == v: return
            if r[u] < r[v]:
                u,v = v,u
            f[v] = u
            if r[u] == r[v]:
                r[u] += 1

        cells_set = set((i,j) for i,j in cells)
        for i in range(1, row+1):
            for j in range(1, col+1):
                if (i,j) in cells_set: continue
                for ni,nj in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                    if ni<1 or nj<1 or ni>row or nj>col or (ni,nj) in cells_set: continue
                    union((i,j), (ni,nj))
        top = (0,0)
        bot = (row+1, col+1)
        for j in range(1, col+1):
            if (1,j) not in cells:
                union((1,j), top)
            if (row,j) not in cells:
                union((row,j), bot)
        if find(top) == find(bot): return len(cells)
        for d in range(len(cells)-1, -1, -1):
            i,j = cells[d]
            cells_set.remove((i,j))
            for ni,nj in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                if ni<1 or nj<1 or ni>row or nj>col or (ni,nj) in cells_set: continue
                union((i,j), (ni,nj))
            if find(top) == find(bot): return d
        return -1