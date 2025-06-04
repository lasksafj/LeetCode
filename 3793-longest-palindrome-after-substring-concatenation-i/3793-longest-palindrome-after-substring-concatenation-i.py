def p(s):
    N = len(s)
    dp = [[0]*N for _ in range(N)]
    res = [1]*N + [0]
    for j in range(N):
        for i in range(j,-1,-1):
            if s[i] == s[j]:
                if i == j:
                    dp[i][j] = 1
                elif i+1 == j:
                    dp[i][j] = 2
                elif dp[i+1][j-1]:
                    dp[i][j] = dp[i+1][j-1] + 2
            res[i] = max(res[i], dp[i][j])
    return res

class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        t = t[::-1]
        ps = p(s)
        pt = p(t)
        
        n1,n2 = len(s), len(t)
        res = 0
        for k in range(-n1, n2):
            a = max(0, -k-1)
            b = max(0, k)
            cur = 0
            while a < n1 and b < n2:
                if s[a] == t[b]:
                    cur += 1
                else:
                    res = max(res, cur*2 + max(ps[a], pt[b]))
                    cur = 0
                a += 1
                b += 1
            if cur:
                res = max(res, cur*2 + max(ps[a], pt[b]))
        return res