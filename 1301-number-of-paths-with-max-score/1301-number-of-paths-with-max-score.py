class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        M,N = len(board),len(board[0])
        dp = [[[-inf,0] for _ in range(N+1)] for _ in range(M+1)]
        MOD = 10**9+7
        dp[0][0] = [0,1]
        for i in range(1, M+1):
            for j in range(1, N+1):
                x = board[i-1][j-1]
                if x == 'X': continue
                elif x in 'SE':
                    x = 0
                else:
                    x = int(x)
                a,b,c = dp[i-1][j], dp[i][j-1], dp[i-1][j-1]
                ma = max(a[0], b[0], c[0])
                way = 0
                for q in [a,b,c]:
                    if q[0] == ma:
                        way += q[1]
                dp[i][j] = [ma+x, way%MOD]
        return dp[-1][-1] if dp[-1][-1][0] > -inf else [0,0]