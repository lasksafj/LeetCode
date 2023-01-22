class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        for j in range(n):
            for i in range(0,j):
                if s[i] == s[j] and (i+1 == j or dp[i+1][j-1]):
                    dp[i][j] = True
        def sol(i):
            if i == len(s):
                res.append(path[:])
            for j in range(i,n):
                if dp[i][j]:
                    path.append(s[i:j+1])
                    sol(j+1)
                    path.pop()
        res = []
        path = []
        sol(0)
        return res