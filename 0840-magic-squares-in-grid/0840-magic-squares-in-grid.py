class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def check(A):
            B = A[0] + A[1] + A[2]
            if len(set(B)) < 9 or max(B) > 9 or min(B) < 1:
                return 0
            if sum(A[0]) != sum(A[1]) or sum(A[1]) != sum(A[2]):
                return 0
            if A[0][0] + A[2][2] != A[0][2] + A[2][0]:
                return 0
            A = list(zip(*A))
            if sum(A[0]) != sum(A[1]) or sum(A[1]) != sum(A[2]):
                return 0
            return 1
            
        M,N = len(grid),len(grid[0])
        res = 0
        for i in range(M-2):
            for j in range(N-2):
                res += check([grid[i][j:j+3]] + [grid[i+1][j:j+3]] + [grid[i+2][j:j+3]])
        return res