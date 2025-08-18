class Solution:
    def lexicographicallySmallestString(self, s: str) -> str:
        N = len(s)
        A = [ord(ch) for ch in s]
        @cache
        def can_empty(i,j):
            if i > j:
                return True
            if abs(A[i]-A[j]) in [1,25] and can_empty(i+1,j-1):
                return True
            return any(can_empty(i,k) and can_empty(k+1,j) for k in range(i+1, j, 2))
        @cache
        def dp(i):
            if i == N:
                return ''
            res = s[i] + dp(i+1)
            for j in range(i+1, N, 2):
                if can_empty(i,j):
                    res = min(res, dp(j+1))
            return res
        return dp(0)