class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        A = [[0]*(query_row+1) for _ in range(query_row+1)]
        A[0][0] = poured
        for i in range(query_row):
            for j in range(i+1):
                if A[i][j] <= 1: continue
                excess = (A[i][j] - 1)/2
                A[i+1][j] += excess
                A[i+1][j+1] += excess
        return min(1, A[query_row][query_glass])