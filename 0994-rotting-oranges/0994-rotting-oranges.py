class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        M,N = len(grid),len(grid[0])
        q = deque()
        oranges = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 2:
                    q.append([i,j])
                oranges += grid[i][j] != 0
        res = -1
        while q:
            oranges -= len(q)
            for _ in range(len(q)):
                i,j = q.popleft()
                for ni,nj in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                    if 0<=ni<M and 0<=nj<N and grid[ni][nj] == 1:
                        q.append([ni,nj])
                        grid[ni][nj] = 2
            res += 1
        return max(0, res) if oranges == 0 else -1