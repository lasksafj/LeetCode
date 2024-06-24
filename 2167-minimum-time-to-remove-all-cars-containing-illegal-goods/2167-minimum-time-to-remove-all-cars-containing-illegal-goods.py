class Solution:
    def minimumTime(self, s: str) -> int:
        N = len(s)
        left = 0
        res = inf
        for i in range(N):
            cur = int(s[i]=='1')
            left = min(left+cur*2, i+1)
            res = min(res, left+N-i-1)
        return res