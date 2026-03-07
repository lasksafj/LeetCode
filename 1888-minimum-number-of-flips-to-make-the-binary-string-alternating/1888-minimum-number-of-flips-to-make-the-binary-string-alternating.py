class Solution:
    def minFlips(self, s: str) -> int:
        def f(s):
            n1,n0 = 0,0
            res = []
            for c in s:
                n0,n1 = n1 + (c!='0'), n0 + (c!='1')
                res.append([n0,n1])
            return res
        A = f(s)
        res = min(A[-1])
        if len(s)&1 == 0:
            return res
        B = f(s[::-1])[::-1]
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                if s[i] == '0':
                    res = min(res, A[i][0] + B[i+1][0], 2 + A[i][1] + B[i+1][1])
                else:
                    res = min(res, A[i][1] + B[i+1][1], 2 + A[i][0] + B[i+1][0])
        return res