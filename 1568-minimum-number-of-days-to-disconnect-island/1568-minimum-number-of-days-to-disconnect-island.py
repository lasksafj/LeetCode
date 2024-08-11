class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        M,N = len(grid),len(grid[0])
        DIRECTIONS = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        
        time = {}   # discovery time of vertex u 
        low = {}    # time of a vertex v discovered before u, lowest time - u can go to v b/c cycle
                    # a--v--u--b
                    #    |_____|
                    # low[u] = time[v] not time[a]
                    
        ap = defaultdict(int)   # whether u is an articulation point 
                                # case 1:
                                # for all children v of u:
                                #   low[u] <= low[v]
                                # case 2:
                                # u is root and number of children of u > 1
        timer = 0
        def dfs(i,j,pi,pj):
            nonlocal timer
            time[i,j] = low[i,j] = timer
            timer += 1
            children = 0
            for ni,nj in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                if not (0<=ni<M and 0<=nj<N and grid[ni][nj] == 1):
                    continue
                if (ni,nj) == (pi,pj):
                    continue
                if (ni,nj) not in time:
                    children += 1
                    dfs(ni,nj,i,j)
                    if time[i,j] <= low[ni,nj]:
                        ap[i,j] = 1
                    low[i,j] = min(low[i,j], low[ni,nj])
                else:
                    low[i,j] = min(low[i,j], time[ni,nj])
            return children
        
        no_island = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1 and (i,j) not in time:
                    ap[i,j] = 1 if dfs(i,j,-1,-1) > 1 else 0
                    no_island += 1
                    
        if no_island == 0 or no_island > 1:
            return 0
        if sum(sum(row) for row in grid) == 1 or sum(ap.values()) > 0:
            return 1
        return 2
                