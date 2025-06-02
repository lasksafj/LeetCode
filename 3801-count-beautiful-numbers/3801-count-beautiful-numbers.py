class Solution:
    def beautifulNumbers(self, l: int, r: int) -> int:
        # for 1<=n<=10^9: only about 4000 distinct product
        def f(A):
            A = [int(c) for c in str(A)]
            @cache
            def dfs(i, tight, lead_zero, p, s):
                if i == len(A):
                    return s and p%s == 0
                ma = A[i] if tight else 9
                res = 0
                for d in range(ma+1):
                    new_p = p * (1 if lead_zero and d==0 else d)
                    res += dfs(i+1, tight&(d==ma), lead_zero&(d==0), new_p, s+d)
                return res
            return dfs(0, 1, 1, 1, 0)
        return f(r) - f(l-1)