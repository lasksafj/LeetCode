class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        M,N = len(heightMap),len(heightMap[0])
        if M==1 or N==1:
            return 0
        pq = []
        vis = set()
        for i in range(M):
            heappush(pq, [heightMap[i][0], i,0])
            heappush(pq, [heightMap[i][N-1], i,N-1])
            vis.add((i,0))
            vis.add((i,N-1))
        for j in range(N):
            heappush(pq, [heightMap[0][j], 0,j])
            heappush(pq, [heightMap[M-1][j], M-1,j])
            vis.add((0,j))
            vis.add((M-1,j))
        res = 0
        while pq:
            h,i,j = heappop(pq)
            for ni,nj in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                if 0<=ni<M and 0<=nj<N and (ni,nj) not in vis:
                    res += max(0, h - heightMap[ni][nj])
                    heappush(pq, [max(heightMap[ni][nj], h), ni,nj])
                    vis.add((ni,nj))
        return res