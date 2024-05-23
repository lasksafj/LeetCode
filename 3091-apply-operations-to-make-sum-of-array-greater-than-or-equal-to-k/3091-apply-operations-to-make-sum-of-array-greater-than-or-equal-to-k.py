class Solution:
    def minOperations(self, k: int) -> int:
        res = inf
        for a in range(k):
            b = ceil(k/(1+a))-1
            res = min(res, a+b)
        return res