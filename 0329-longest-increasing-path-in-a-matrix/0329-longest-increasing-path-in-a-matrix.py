class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        M,N = len(matrix),len(matrix[0])
        F = lambda a,b: a*N+b
        adj = [[] for _ in range(M*N)]
        ind = [0]*(M*N)
        for i in range(M):
            for j in range(N):
                for ni,nj in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                    if 0<=ni<M and 0<=nj<N and matrix[ni][nj] > matrix[i][j]:
                        adj[F(i,j)].append(F(ni,nj))
                        ind[F(ni,nj)] += 1
        q = deque()
        dist = [0]*(M*N)
        for i in range(M*N):
            if ind[i] == 0:
                q.append(i)
                dist[i] = 1
        
        while q:
            cur = q.popleft()
            for ne in adj[cur]:
                dist[ne] = max(dist[ne], dist[cur]+1)
                ind[ne] -= 1
                if ind[ne] == 0:
                    q.append(ne)
        return max(dist)