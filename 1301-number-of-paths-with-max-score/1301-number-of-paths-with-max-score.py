class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        M,N = len(board),len(board[0])
        dp1 = [[-inf]*(N+1) for _ in range(M+1)]
        # dp1[-1][-1] = 0
        dp2 = [[0]*(N+1) for _ in range(M+1)]
        # dp2[-1][-1] = 1
        for i in range(M-1,-1,-1):
            for j in range(N-1,-1,-1):
                if i==M-1 and j==N-1:
                    dp1[i][j] = 0
                    dp2[i][j] = 1
                    continue
                if board[i][j] == 'X':
                    dp1[i][j] = -inf
                    continue
                ma = max(dp1[i][j+1], dp1[i+1][j], dp1[i+1][j+1])
                if ma == dp1[i][j+1]:
                    dp2[i][j] = dp2[i][j+1]
                if ma == dp1[i+1][j]:
                    dp2[i][j] += dp2[i+1][j]
                if ma == dp1[i+1][j+1]:
                    dp2[i][j] += dp2[i+1][j+1]
                dp2[i][j] %= 1000000007
                dp1[i][j] = ma + (int(board[i][j]) if board[i][j] != 'E' else 0)
        # for r in dp1:
        #     print(r)
        return [dp1[0][0],dp2[0][0]] if dp1[0][0] > -inf else [0,0]