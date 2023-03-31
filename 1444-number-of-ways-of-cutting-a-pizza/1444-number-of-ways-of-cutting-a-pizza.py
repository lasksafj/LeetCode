class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        m = len(pizza)
        n = len(pizza[0])
        apples = [[0] * (n + 1) for row in range(m + 1)]
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                apples[i][j] = (pizza[i][j] == 'A') + apples[i+1][j] + apples[i][j+1] - apples[i+1][j+1]
        dp = [[[0 for _ in range(n)] for _ in range(m)] for _ in range(k)]
        dp[0] = [[int(apples[i][j] > 0) for j in range(n)] for i in range(m)]
        for r in range(1,k):
            for i in range(m):
                for j in range(n):
                    val = 0
                    for ne_col in range(j+1, n):
                        if apples[i][j] - apples[i][ne_col] > 0:
                            val += dp[r-1][i][ne_col]
                    for ne_row in range(i+1, m):
                        if apples[i][j] - apples[ne_row][j] > 0:
                            val += dp[r-1][ne_row][j]
                    dp[r][i][j] = val % 1000000007
        return dp[k-1][0][0]