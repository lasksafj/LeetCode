class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        M,N = len(grid),len(grid[0])
        q = deque()
        safe = [[-1]*N for _ in range(M)]
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    q.append([i,j])
                    safe[i][j] = 0
        k = 1
        while q:
            for _ in range(len(q)):
                i,j = q.popleft()
                for ni,nj in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                    if 0<=ni<M and 0<=nj<N and safe[ni][nj] == -1:
                        safe[ni][nj] = k
                        q.append([ni,nj])
            k += 1
        pq = [[-safe[0][0], 0,0]]
        dist = [[0]*N for _ in range(M)]
        dist[0][0] = safe[0][0]
        while pq:
            cur,i,j = heappop(pq)
            cur = -cur
            if (i,j) == (M-1,N-1):
                return cur
            if cur < dist[i][j]: continue
            for ni,nj in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                if 0<=ni<M and 0<=nj<N:
                    h = min(cur, safe[ni][nj])
                    if dist[ni][nj] < h:
                        dist[ni][nj] = h
                        heappush(pq, [-h,ni,nj])
        return dist[-1][-1]