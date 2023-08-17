class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        M,N = len(mat),len(mat[0])
        res = [[inf]*N for _ in range(M)]
        q = deque()
        for i in range(M):
            for j in range(N):
                if mat[i][j] == 0:
                    q.append((i,j))
                    res[i][j] = 0
        step = 0
        while q:
            step += 1
            for _ in range(len(q)):
                x,y = q.popleft()
                for nx,ny in [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]:
                    if 0 <= nx < M and 0 <= ny < N and res[nx][ny] == inf:
                        res[nx][ny] = step
                        q.append((nx,ny))
        return res