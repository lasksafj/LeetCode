class Solution:
    def minimumCost(self, s: str) -> int:
        n = len(s)
        dpr = [[0]*2 for _ in range(n)]
        dpl = [[0]*2 for _ in range(n)]
        @cache
        def f(i,ch, d):
            if (i == 0 and d==-1) or (i == n-1 and d==1):
                return 0 if ch==0 else 1
            if ch == 0:
                return f(i+d, (0 if s[i+d]==s[i] else 1), d)
            else:
                return f(i+d, (0 if s[i+d]==s[i] else 1), d) + (n-i if d>0 else i+1)
            # return dp[i]
        # print(f(2,1,-1))
        res = inf
        for i in range(n-1):
            if s[i] == s[i+1]:
                res = min(res, f(i,0,-1) + f(i+1,0,1), f(i,1,-1) + f(i+1,1,1))
            else:
                res = min(res, f(i,0,-1) + f(i+1,1,1), f(i,1,-1) + f(i+1,0,1))
        return min(res, f(0,0,1), f(0,1,1), f(n-1,0,-1), f(n-1,1,-1))

        
        