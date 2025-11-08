# number of op to change 2^k -> 0
@cache
def f(k):
    if k == 0:
        return 1
    return f(k-1)*2 + 1
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        def dfs(n):
            if n == 0:
                return 0
            k = len(bin(n))-3
            return f(k) - dfs(n^(1<<k))
        return dfs(n)