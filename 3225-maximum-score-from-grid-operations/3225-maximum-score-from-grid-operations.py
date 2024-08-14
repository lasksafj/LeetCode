class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        N = len(grid)
        B = [list(accumulate(col, initial=0)) for col in zip(*grid)]
        dp1 = [0]*(N+1)
        dp2 = [0]*(N+1)
        for j in range(1, N):
            ndp1 = [0]*(N+1)
            ndp2 = [0]*(N+1)
            pre1 = B[j-1]
            pre2 = B[j]
            for k in range(N+1):
                for i in range(N+1):
                    d1 = pre1[i]-pre1[k] if i>=k else 0
                    ndp1[i] = max( ndp1[i], max(d1, dp2[k]-dp1[k]) + dp1[k] )  
                    d2 = pre2[k]-pre2[i] if k>=i else 0
                    ndp2[i] = max(ndp2[i], max(d1, dp2[k]-dp1[k]) + dp1[k] + d2)
            dp1 = ndp1
            dp2 = ndp2
            # print(dp1,dp2)
        return max(dp2)