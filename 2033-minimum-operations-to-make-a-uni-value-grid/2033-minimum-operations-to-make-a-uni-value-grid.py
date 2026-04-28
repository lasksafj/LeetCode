class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        A = []
        for row in grid:
            for n in row:
                A.append(n)
        A.sort()
        res = 0
        mi = A[len(A)//2]
        for a in A:
            if abs(mi-a)%x != 0: return -1
            res += abs(mi-a)//x
        return res