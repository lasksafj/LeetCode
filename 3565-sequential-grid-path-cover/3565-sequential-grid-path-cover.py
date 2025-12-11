class Solution:
    def findPath(self, grid: List[List[int]], k: int) -> List[List[int]]:
        M,N = len(grid),len(grid[0])
        q = deque()
        prev = defaultdict(tuple)
        for d in range(M*N):
            mask = 1<<d
            i,j = d//N, d%N
            if grid[i][j] > 1: continue
            q.append([i,j,mask,grid[i][j]])
            prev[i,j,mask] = (-1,-1,-1)
        ok = False
        while q:
            i,j,mask,d = q.popleft()
            if mask == (1<<(M*N)) - 1:
                ok = True
                break
            for ni,nj in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                if 0<=ni<M and 0<=nj<N and (1<<(ni*N+nj)) & mask == 0 and (grid[ni][nj] == d+1 or grid[ni][nj] == 0):
                    nmask = mask | (1<<(ni*N+nj))
                    if (ni,nj,nmask) in prev: continue
                    q.append([ni,nj,nmask, max(d, grid[ni][nj])])
                    prev[ni,nj,nmask] = (i,j,mask)
        if not ok: return []
        res = []
        while i != -1:
            res.append([i,j])
            i,j,mask = prev[(i,j,mask)]
        return res[::-1]