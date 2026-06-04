class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def sol(n):
            A = [int(c) for c in str(n)]
            @cache
            def dfs(i, tight, leading_zero, a,b):
                if i == len(A):
                    return 0
                ma = A[i] if tight else 9
                res = 0
                for d in range(ma+1):
                    if leading_zero and d == 0:
                        res += dfs(i+1, tight&(d==ma), leading_zero&(d==0), -1, -1)
                    else:
                        if tight&(d==ma):
                            suffix_str = "".join(map(str, A[i+1:]))
                            ways = int(suffix_str) + 1 if suffix_str else 1
                        else:
                            ways = 10 ** (len(A) - i - 1)
                        res += dfs(i+1, tight&(d==ma), leading_zero&(d==0), b, d) + (a > -1 and b > -1 and ((b > d and b > a) or (b < d and b < a)) * ways)
                return res
            return dfs(0, 1, 1, -1,-1)
        return sol(num2) - sol(num1-1)