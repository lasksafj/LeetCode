def Z_func(s):
    N = len(s)
    res = [0]*N
    l,r = 0,0
    for i in range(1,N):
        if i < r:
            res[i] = min(res[i-l], r-i)
        while i+res[i] < N and s[res[i]] == s[i+res[i]]:
            res[i] += 1
        if i+res[i] > r:
            l = i
            r = i+res[i]
    return res

class Solution:
    def numberOfWays(self, s: str, t: str, k: int) -> int:
        n = len(s)
        s = t+'#'+s+s
        Z = Z_func(s)
        
        mod = 10**9+7
        # a(k) # number of way rotate s by 0 in k step
        # b(k) # number of way rotate s by x in k step, 0 < x < N
        # a(k) = (n-1)*b(k-1)
        # b(k) = (n-2)*b(k-1) + a(k-1)
        # solve Recurrence Relation
        # b(0) = 0, b(1) = 1
        # b(k) = ((n - 1)^k - (-1)^k) / n
        # a(k) = ((n - 1)^k - (-1)^k) / n + (-1)^k
        
        a = (pow((n - 1),k,mod) - (-1)**k) * pow(n,-1,mod) + (-1)**k
        b = (pow((n - 1),k,mod) - (-1)**k) * pow(n,-1,mod)
        
        res = 0
        for i in range(n+1, 2*n+1):
            if Z[i] == n:
                if i == n+1:
                    res = (res + a)%mod
                else:
                    res = (res + b)%mod
        return res