class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        M,N = len(moveTime), len(moveTime[0])
        pq = [[0, 0,0,1]]
        vis = [[False]*N for _ in range(M)]
        vis[0][0] = True
        while pq:
            t,i,j,a = heappop(pq)
            if (i,j) == (M-1,N-1):
                return t
            for ni,nj in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                if 0<=ni<M and 0<=nj<N and not vis[ni][nj]:
                    nt = max(t, moveTime[ni][nj]) + a
                    na = 3-a
                    vis[ni][nj] = True
                    heappush(pq, [nt,ni,nj,na])
        return vis[M-1][N-1]