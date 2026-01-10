class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        A = [ord(c) for c in s1]
        B = [ord(c) for c in s2]
        @cache
        def dfs(i,j):
            if i == len(A):
                return sum(B[j:])
            if j == len(B):
                return sum(A[i:])
            if A[i] == B[j]:
                return dfs(i+1,j+1)
            return min(dfs(i+1, j) + A[i], dfs(i,j+1) + B[j], dfs(i+1,j+1) + A[i]+B[j])
        return dfs(0,0)