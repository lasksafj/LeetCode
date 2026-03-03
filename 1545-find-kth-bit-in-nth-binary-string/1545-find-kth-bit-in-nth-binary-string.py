class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def dfs(n,k):
            if n == 1:
                return 0
            l = (1<<n) - 1
            if k <= l//2:
                return dfs(n-1, k)
            elif k == l//2+1:
                return 1
            return dfs(n, l//2 - (k-l//2-1) + 1) ^ 1
        return str(dfs(n,k))