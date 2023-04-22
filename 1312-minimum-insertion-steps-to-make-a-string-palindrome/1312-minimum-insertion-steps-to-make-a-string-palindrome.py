class Solution:
    def minInsertions(self, s: str) -> int:
        sr = s[::-1]
        n = len(s)
        lcsubseq = [[0]*(n+1) for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, n+1):
                if s[i-1] == sr[j-1]:
                    lcsubseq[i][j] = 1 + lcsubseq[i-1][j-1]
                else:
                    lcsubseq[i][j] = max(lcsubseq[i-1][j], lcsubseq[i][j-1])
        return n - lcsubseq[n][n]
        