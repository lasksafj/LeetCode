class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        M,N = len(grid),len(grid[0])
        A = []
        for j in range(N):
            for i in range(M):
                if grid[i][j] == 1:
                    A.append(j)
        med_j = (A[len(A)//2] + A[(len(A)-1)//2])//2

        A = []
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    A.append(i)
        med_i = (A[len(A)//2] + A[(len(A)-1)//2])//2

        return sum(abs(i-med_i) + abs(j-med_j) for i in range(M) for j in range(N) if grid[i][j] == 1)