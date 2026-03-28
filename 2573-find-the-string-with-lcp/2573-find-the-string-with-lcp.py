class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        N = len(lcp)
        s = [0]*N
        c = 0
        for i in range(N):
            if s[i]: continue
            c += 1
            if c > 26: return ''
            s[i] = c
            for j in range(i+1,N):
                if lcp[i][j] > 0:
                    if s[j]: return ''
                    s[j] = c
        dp = [[0]*N for _ in range(N)]
        for i in range(N-1,-1,-1):
            for j in range(N-1,-1,-1):
                if s[i] == s[j]:
                    if i+1 < N and j+1 < N:
                        dp[i][j] = dp[i+1][j+1] + 1
                    else:
                        dp[i][j] = 1
        if dp != lcp: return ''
        a = ord('a')
        return ''.join(chr(c+a-1) for c in s)