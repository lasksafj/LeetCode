class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        N = len(grid)
        A = [0]*N
        for i,row in enumerate(grid):
            for j in range(N-1, -1, -1):
                if row[j] == 1:
                    A[i] = j
                    break
        res = 0
        for i in range(N):
            ok = False
            for j in range(i, N):
                if A[j] <= i:
                    res += j-i
                    A = [0] + A[:j] + A[j+1:]
                    ok = True
                    break
            if not ok: return -1
        return res