class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m,n = len(grid),len(grid[0])
        dp = [i for i in range(n)]
        for row in grid:
            tmp = [-1] * n
            for i in range(n-1):
                if row[i] == row[i+1]:
                    if row[i] == 1 and dp[i] > -1:
                        tmp[i+1] = dp[i]
                    if row[i] == -1 and dp[i+1] > -1:
                        tmp[i] = dp[i+1]
            dp = tmp
        res = [-1] * n
        for i,v in enumerate(dp):
            res[v] = i if v > -1 else res[v]
        return res