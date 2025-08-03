class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total = sum(sum(r) for r in grid)
        def sol(A):
            def f(A):
                cur = 0
                s = set()
                for i,row in enumerate(A):
                    cur += sum(row)
                    if cur - (total-cur) in [0, A[0][0], A[0][-1], A[i][0]]:
                        return True
                    s |= set(row)
                    if len(row) > 1 and i > 0 and cur - (total-cur) in s:
                        return True
                return False
            return f(A) or f(A[::-1])
        return sol(grid) or sol(list(zip(*grid)))