class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        mod = 10**9+7
        dp = [[0]*(target+1) for _ in range(len(types)+1)]
        for i in range(len(types)):
            dp[i][0] = 1
        for i in range(1, len(types)+1):
            for j in range(1, target+1):
                dp[i][j] = dp[i-1][j]
                a = j - types[i-1][1]
                b = types[i-1][0] - 1
                while a >= 0 and b >= 0:
                    dp[i][j] = (dp[i][j] + dp[i-1][a]) % mod
                    a -= types[i-1][1]
                    b -= 1
        return dp[-1][target] % mod