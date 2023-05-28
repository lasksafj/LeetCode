class Solution:
    def minimumCost(self, s: str) -> int:
        n = len(s)
        res = 0
        for i in range(n):
            if i > 0 and s[i] != s[i-1]:
                res += min(i, n-i)
        return res
