class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        ma = max(costs)
        A = [0]*(ma+1)
        for c in costs:
            A[c] += 1
        res = 0
        for c,v in enumerate(A):
            if v == 0: continue
            d = min(v, coins//c)
            res += d
            coins -= d*c
        return res