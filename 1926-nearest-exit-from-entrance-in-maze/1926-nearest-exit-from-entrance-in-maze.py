class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m,n = len(maze),len(maze[0])
        q = deque([entrance])
        vis = [[0] * n for _ in range(m)]
        vis[entrance[0]][entrance[1]] = 1
        res = 0
        while q:
            s = len(q)
            res += 1
            for _ in range(s):
                x,y = q.popleft()
                for a,b in ([1,0],[0,1],[-1,0],[0,-1]):
                    nx,ny = x+a,y+b
                    if nx >= 0 and nx < m and ny >= 0 and ny < n \
                        and not vis[nx][ny] and maze[nx][ny] == '.':
                        if nx == 0 or nx == m-1 or ny == 0 or ny == n-1:
                            return res
                        q.append([nx,ny])
                        vis[nx][ny] = 1
        return -1