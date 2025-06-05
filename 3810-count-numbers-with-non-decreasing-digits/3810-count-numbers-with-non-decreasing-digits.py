class Solution:
    def countNumbers(self, l: str, r: str, b: int) -> int:
        def divide(s,b):
            res = ''
            n = 0
            for d in s:
                n = n*10 + int(d)
                res += str(n//b)
                n %= b
            return ''.join(res).lstrip('0') or '0', n
        def base(s,b):
            res = []
            while s != '0':
                s, rem = divide(s,b)
                res.append(str(rem))
            return ''.join(res[::-1])
        def minus_one(s):
            carry = 1
            res = []
            for d in s[::-1]:
                d = int(d)
                res.append(str((d+10-carry)%10))
                if d >= carry:
                    carry = 0
            return ''.join(res[::-1])
        
        MOD = 10**9+7
        def f(x):
            A = [int(d) for d in base(x,b)]
            @cache
            def dfs(i,p, tight):
                if i == len(A):
                    return 1
                ma = A[i] if tight else b-1
                res = 0
                for d in range(p, ma+1):
                    res += dfs(i+1, d, tight&(d==ma))
                return res % MOD
            return dfs(0, 0, 1)
        return (f(r) - f(minus_one(l))) % MOD