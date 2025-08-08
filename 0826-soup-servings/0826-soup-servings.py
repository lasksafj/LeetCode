@cache
def dfs(a,b):
    if a <= 0 and b <= 0:
        return 0.5
    if a <= 0:
        return 1
    if b <= 0:
        return 0
    return 0.25 * (dfs(a-4,b) + dfs(a-3,b-1) + dfs(a-2,b-2) + dfs(a-1,b-3))

class Solution:
    def soupServings(self, n: int) -> float:
        res = 0.5
        for i in range(1, ceil(n/25)+1):
            res = dfs(i,i)
            if res > 1-1e-5:
                return 1
        return res