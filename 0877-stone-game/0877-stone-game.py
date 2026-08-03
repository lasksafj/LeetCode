class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        piles = [0] + piles + [0]
        s = sum(piles)
        dp = [[[0]*2 for _ in range(n+2)] for _ in range(n+2)]
        for i in range(1, n+1):
            for j in range(n, i, -1):
                for a in [0,1]:
                    dp[i][j][a] = max(dp[i-1][j][a^1] + piles[i], dp[i][j+1][a^1] + piles[j])
            ans = max(dp[i][i+1])
            if ans > s-ans:
                return True
        return False