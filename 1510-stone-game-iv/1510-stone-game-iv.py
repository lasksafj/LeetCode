class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [[0]*2 for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(n+1):
            for t in [0,1]:
                mi = 1
                for a in range(1, int(sqrt(i))+1):
                    a *= a
                    if dp[i-a][t^1] == 0:
                        mi = 0
                        break
                dp[i][t] = mi^1
        return True if dp[n][1] else False