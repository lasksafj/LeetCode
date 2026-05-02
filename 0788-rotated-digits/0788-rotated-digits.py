class Solution:
    def rotatedDigits(self, n: int) -> int:
        A = [int(a) for a in str(n)]
        @cache
        def dfs(i, tight, k):
            if i == len(A):
                return k
            ma = A[i] if tight else 9
            res = 0
            for d in range(ma+1):
                if d not in [0,1,8,2,5,6,9]:
                    continue
                kk = k
                if d in [2,5,6,9]:
                    kk = 1
                res += dfs(i+1, tight&(d==ma), kk)
            return res
        return dfs(0, 1, 0)