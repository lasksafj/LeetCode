class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        M,N = len(moveTime), len(moveTime[0])
        pq = [[0, 0,0,1]]
        vis = [[inf]*N for _ in range(M)]
        while pq:
            t,i,j,a = heappop(pq)
            for ni,nj in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                if 0<=ni<M and 0<=nj<N:
                    nt = max(t, moveTime[ni][nj]) + a
                    na = 3-a
                    if vis[ni][nj] > nt:
                        vis[ni][nj] = nt
                        heappush(pq, [nt,ni,nj,na])
        return vis[M-1][N-1]