class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        M,N = len(land),len(land[0])
        res = []
        for i in range(M):
            for j in range(N):
                if land[i][j]:
                    r = i
                    while r < M and land[r][j]:
                        c = j
                        while c < N and land[r][c]:
                            land[r][c] = 0
                            c += 1
                        r += 1
                    res.append([i,j,r-1,c-1])
        return res