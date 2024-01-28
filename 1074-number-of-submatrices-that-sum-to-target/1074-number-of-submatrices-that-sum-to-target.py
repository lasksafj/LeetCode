class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        M,N = len(matrix),len(matrix[0])
        A = [[0]*(N+1) for _ in range(M)]
        for i in range(M):
            for j in range(N):
                A[i][j+1] = A[i][j] + matrix[i][j]
        res = 0
        for j2 in range(N+1):
            for j1 in range(j2):
                mp = defaultdict(int)
                s = 0
                mp[0] = 1
                for i in range(M):
                    s += A[i][j2] - A[i][j1]
                    if s-target in mp:
                        res += mp[s-target]
                    mp[s] += 1
        return res