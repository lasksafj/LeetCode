class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        s = sum(sum(row) for row in grid)

        def f(A):
            M,N = len(A), len(A[0])
            a = 0
            if N == 1:
                for i in range(M):
                    a += A[i][0]
                    if a*2 == s or (a-A[i][0])*2 == s-A[i][0] or (a-A[0][0])*2 == s-A[0][0]:
                        return True   
                return False
            a = sum(A[0])
            S = set(A[0])
            if a*2 == s: return True
            for j in [0,N-1]:
                if (a-A[0][j])*2 == s-A[0][j]:
                    return True
            for i in range(1,M):
                S.update(A[i])
                a += sum(A[i])
                if a*2 == s: return True
                if 2*a-s in S: return True
                if a*2 > s: break
            return False


        A = grid
        if f(A) or f(A[::-1]): return True
        A = list(zip(*A))
        return f(A) or f(A[::-1])