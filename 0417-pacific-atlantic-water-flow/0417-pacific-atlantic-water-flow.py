class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        M,N = len(heights),len(heights[0])
        
        def bfs(q):
            res = []
            vis = set(q)
            while q:
                res += list(q)
                for _ in range(len(q)):
                    i,j = q.popleft()
                    for ni,nj in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                        if 0<=ni<M and 0<=nj<N and (ni,nj) not in vis and heights[ni][nj] >= heights[i][j]:
                            q.append((ni,nj))
                            vis.add((ni,nj))
                    
            return res
        
        q = deque([])
        for i in range(M):
            q.append((i,0))
        for j in range(N):
            q.append((0,j))
        pacific = set(bfs(q))
        
        q = deque([])
        for i in range(M):
            q.append((i,N-1))
        for j in range(N):
            q.append((M-1,j))
        atlantic = bfs(q)
        
        res = set()
        for i,j in atlantic:
            if (i,j) in pacific:
                res.add((i,j))
        return list(res)