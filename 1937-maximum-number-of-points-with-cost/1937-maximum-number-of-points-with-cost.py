class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        N = len(points[0])
        dp = points[0]
        for row in points[1:]:
            ndp = [0]*N
            A = [dp[0]]
            for i in range(1,N):
                A.append(max(A[i-1]-1, dp[i]))
            A.append(0)
            for i in range(N-1,-1,-1):
                A[i] = max(A[i], A[i+1]-1)
            for i,p in enumerate(row):
                ndp[i] = A[i] + p
            
            dp = ndp
        return max(dp)