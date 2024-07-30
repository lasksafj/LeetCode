class Solution:
    def minimumDeletions(self, s: str) -> int:
        N = len(s)
        L = [0]*(N)
        d = 0
        for i,ch in enumerate(s):
            d += (ch=='a')
            L[i] = d
        R = [0]*(N)
        d = 0
        for i in range(N-1,-1,-1):
            ch = s[i]
            d += (ch=='a')
            R[i] = d
        res = min(R[0], N-R[0])
        for i,ch in enumerate(s):
            if ch == 'b':
                res = min(res, i - L[i] + R[i])
        return res