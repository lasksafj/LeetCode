class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        A = [[0]*n for _ in range(m)]
        for a,b in guards:
            A[a][b] = 1
        for a,b in walls:
            A[a][b] = 1
        for i,j in guards:
            ni = i+1
            while ni < m and A[ni][j] != 1:
                A[ni][j] = -1
                ni += 1
            ni = i-1
            while ni >= 0 and A[ni][j] != 1:
                A[ni][j] = -1
                ni -= 1
            nj = j+1
            while nj < n and A[i][nj] != 1:
                A[i][nj] = -1
                nj += 1
            nj = j-1
            while nj >= 0 and A[i][nj] != 1:
                A[i][nj] = -1
                nj -= 1
        return sum(1 if e==0 else 0 for row in A for e in row)