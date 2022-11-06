class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        m,n = len(robot),len(factory)
        dp = [[inf]*n for _ in range(m)]
        for j in range(n):
            limit = factory[j][1]
            for i in range(m):
                dp[i][j] = dp[i][j-1] if j > 0 else inf
                s = 0
                for k in range(i, max(-1, i-limit), -1):
                    s += abs(robot[k] - factory[j][0])
                    if j <= 0:
                        a = inf
                    if k <= 0:
                        a = 0
                    if k > 0 and j > 0:
                        a = dp[k-1][j-1]
                    dp[i][j] = min(dp[i][j], a + s)
                    # dp[i][j] = min(dp[i][j], (dp[k-1][j-1] if k>0 and j>0 else 0) + s)
                    # print(j, i, k, s, dp[j-1][j])
        # print(dp)
        return dp[m-1][n-1]