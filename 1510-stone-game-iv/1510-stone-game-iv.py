class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [0]*(n+1)
        for i in range(n+1):
            mi = 1
            for a in range(1, int(sqrt(i))+1):
                a *= a
                if dp[i-a] == 0:
                    mi = 0
                    break
            dp[i] = mi^1
        return True if dp[n] else False