class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        def dist(a,b,c,d):
            return abs(a-c) + abs(b-d)
        
        q = []
        n = len(grid)
        A = [[inf]*n for _ in range(n)]
        vis = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    if (i==0 and j==0) or (i==n-1 and j==n-1):
                        return 0
                    A[i][j] = 0
                    q.append((0,i,j))
        while q:
            s,i,j = heappop(q)
            for ni,nj in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                if 0<=ni<n and 0<=nj<n and A[ni][nj] > s+1:
                    A[ni][nj] = s+1
                    heappush(q, (s+1,ni,nj))

        q = [(-A[0][0],0,0)]
        vis = [[0]*n for _ in range(n)]
        vis[0][0] = A[0][0]
        while q:
            # print(q)
            s,i,j = heappop(q)
            s = -s
            if i==n-1 and j==n-1:
                return s

            for ni,nj in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                if 0<=ni<n and 0<=nj<n and vis[ni][nj] < min(s, A[ni][nj]):
                    d = min(s, A[ni][nj])
                    heappush(q, (-d, ni,nj))
                    vis[ni][nj] = d
            
        return 0