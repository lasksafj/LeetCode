class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        R, C = len(isInfected), len(isInfected[0])
        def neighbors(r, c):
            for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc
        vis = set()
        def dfs(i,j):
            if (i,j) not in vis:
                vis.add((i,j))
                regions[-1].add((i,j))
                for ni,nj in neighbors(i,j):
                    if isInfected[ni][nj] == 1:
                        dfs(ni,nj)
                    elif isInfected[ni][nj] == 0:
                        frontiers[-1].add((ni, nj))
                        perimeters[-1] += 1
        res = 0
        while True:
            vis = set()
            regions = []
            frontiers = []
            perimeters = []
            for i in range(R):
                for j in range(C):
                    if isInfected[i][j] == 1 and (i,j) not in vis:
                        regions.append(set())
                        frontiers.append(set())
                        perimeters.append(0)
                        dfs(i,j)
            if not regions:
                break
            idx = frontiers.index(max(frontiers, key=len))
            res += perimeters[idx]
            for i,reg in enumerate(regions):
                if i == idx:
                    for a,b in reg:
                        isInfected[a][b] = -1
                else:
                    for a,b in reg:
                        for na,nb in neighbors(a, b):
                            if isInfected[na][nb] == 0:
                                isInfected[na][nb] = 1
        return res