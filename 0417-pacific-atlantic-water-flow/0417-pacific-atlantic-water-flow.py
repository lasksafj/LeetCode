class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        M,N = len(heights),len(heights[0])
        def bfs(q):
            vis = set(q)
            while q:
                i,j = q.popleft()
                for ni,nj in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                    if 0<=ni<M and 0<=nj<N and (ni,nj) not in vis and heights[ni][nj] >= heights[i][j]:
                        vis.add((ni,nj))
                        q.append((ni,nj))
            return vis
        A = deque()
        P = deque()
        for i in range(M):
            P.append((i,0))
            A.append((i,N-1))
        for j in range(N):
            P.append((0,j))
            A.append((M-1,j))
        return list(bfs(A) & bfs(P))