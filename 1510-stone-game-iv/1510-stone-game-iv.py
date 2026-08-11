class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        sq = []
        for i in range(1, int(sqrt(n))+1):
            sq.append(i*i)
        dp = [[0]*2 for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(n+1):
            for t in [0,1]:
                mi = 1
                for a in sq:
                    if i-a < 0: break
                    mi = min(mi, dp[i-a][t^1])
                dp[i][t] = mi^1
        return True if dp[n][1] else False