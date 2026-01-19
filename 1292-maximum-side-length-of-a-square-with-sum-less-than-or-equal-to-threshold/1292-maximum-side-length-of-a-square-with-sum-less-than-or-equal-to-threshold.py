class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        M,N = len(mat), len(mat[0])
        A = [[0]*(N+1) for _ in range(M+1)]
        for i in range(1, M+1):
            for j in range(1, N+1):
                A[i][j] = A[i-1][j] + A[i][j-1] - A[i-1][j-1] + mat[i-1][j-1]
        for row in A:
            print(row)
        def check(mi):
            for i in range(M+1-mi):
                for j in range(N+1-mi):
                    if A[i+mi][j+mi] - A[i+mi][j] - A[i][mi+j] + A[i][j] <= threshold:
                        return True
            return False
        l,r = 1,min(M,N)
        while l <= r:
            mi = (l+r)//2
            if check(mi):
                l = mi+1
            else:
                r = mi-1
        return r