class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        vis = set()
        isl_a = deque()
        n = len(grid)
        def dfs(i,j):
            if i>=0 and i<n and j>=0 and j<n:
                if (i,j) not in vis and grid[i][j] == 1:
                    vis.add((i,j))
                    isl_a.append((i,j))
                    dfs(i+1,j)
                    dfs(i,j+1)
                    dfs(i-1,j)
                    dfs(i,j-1)
        
        found = False
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i,j)
                    found = True
                    break
            if found:
                break
        res = -1
        while isl_a:
            res += 1
            for _ in range(len(isl_a)):
                i,j = isl_a.popleft()
                for dx,dy in [[0,1],[1,0],[0,-1],[-1,0]]:
                    ni,nj = i+dx,j+dy
                    if (ni,nj) not in vis and ni>=0 and ni<n and nj>=0 and nj<n:
                        if grid[ni][nj] == 1:
                            return res
                        isl_a.append((ni,nj))
                        vis.add((ni,nj))
        return -1