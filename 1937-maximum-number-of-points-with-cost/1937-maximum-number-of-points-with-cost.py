class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        N = len(points[0])
        dp = points[0]
        for row in points[1:]:
            ndp = [0]*N
            A = []
            ma,ma_i = 0,0
            for i in range(N):
                cur = ma-abs(i-ma_i)
                if dp[i] > cur:
                    ma = dp[i]
                    ma_i = i
                    cur = ma
                A.append([cur,ma_i])
            ma,ma_i = 0,0
            for i in range(N-1,-1,-1):
                cur = ma-abs(i-ma_i)
                if dp[i] > cur:
                    ma = dp[i]
                    ma_i = i
                    cur = ma
                if cur > A[i][0]:
                    A[i] = [cur,ma_i]
            for i,p in enumerate(row):
                ndp[i] = A[i][0] + p
            
            dp = ndp
        return max(dp)