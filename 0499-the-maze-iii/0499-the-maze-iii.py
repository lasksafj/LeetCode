class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        M,N = len(maze),len(maze[0])
        def get_neighbor(i,j):
            directions = [(0, -1, 'l'), (-1, 0, 'u'), (0, 1, 'r'), (1, 0, 'd')]
            res = []
            for dx, dy, direction in directions:
                ni,nj = i,j
                d = 0
                while 0 <= ni+dx < M and 0 <= nj+dy < N and maze[ni+dx][nj+dy] == 0:
                    ni += dx
                    nj += dy
                    d += 1
                    if [ni,nj] == hole:
                        break
                res.append([ni,nj,d,direction])
            return res

        pq = [[0, ''] + ball]
        vis = set()
        vis.add(tuple(ball))
        while pq:
            cur,path,i,j = heappop(pq)
            if [i,j] == hole:
                return path
            vis.add((i,j))
            for ni,nj,d,direction in get_neighbor(i,j):
                if (ni,nj) in vis:
                    continue
                heappush(pq, [cur+d, path+direction, ni,nj])
        return 'impossible'