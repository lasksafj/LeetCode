class Solution:
    def checkRecord(self, n: int) -> int:

        
        dp = [[1]*4 for _ in range(3)]
        for na in range(2):
            dp[na][3] = 0
        for nl in range(4):
            dp[2][nl] = 0
        # for e in dp:
        #     print(e)
        for i in range(n):
            ndp = [e[:] for e in dp]
            for na in range(2):
                for nl in range(3):
                    ndp[na][nl] = (dp[na+1][0] + dp[na][0] + dp[na][nl+1]) % 1000000007
            dp = ndp
        return dp[0][0]