class Solution:
    def spiralMatrixIII(self, M: int, N: int, rStart: int, cStart: int) -> List[List[int]]:
        A = [[0,1],[1,0],[0,-1],[-1,0]]
        step = 0
        d = 0
        i,j = rStart, cStart
        res = [[i,j]]
        while len(res) < M*N:
            if d%2 == 0:
                step += 1
            for k in range(step):
                i,j = i+A[d][0], j+A[d][1]
                if 0<=i<M and 0<=j<N:
                    res.append([i,j])
            d = (d+1)%4
        return res