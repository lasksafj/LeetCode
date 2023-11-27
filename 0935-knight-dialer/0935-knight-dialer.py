class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        dp = [1]*10
        for _ in range(1,n):
            ndp = [0]*10
            for i in range(10):
                if i == 5:
                    ndp[i] = 0
                elif i == 0:
                    ndp[i] = dp[4] + dp[6]
                elif i == 1:
                    ndp[i] = dp[6] + dp[8]
                elif i == 2:
                    ndp[i] = dp[7] + dp[9]
                elif i == 3:
                    ndp[i] = dp[4] + dp[8]
                elif i == 4:
                    ndp[i] = dp[3] + dp[0] + dp[9]
                elif i == 6:
                    ndp[i] = dp[1] + dp[7] + dp[0]
                elif i == 7:
                    ndp[i] = dp[2] + dp[6]
                elif i == 8:
                    ndp[i] = dp[1] + dp[3]
                else:
                    ndp[i] = dp[2] + dp[4]
            dp = ndp
            # print(dp)
            # print(sum(dp))
        return sum(dp)%1000000007