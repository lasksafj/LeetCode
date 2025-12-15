class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        l = 1
        res = 0
        prev = -inf
        for p in prices:
            if p == prev-1:
                l += 1
            else:
                l = 1
            prev = p
            res += l
        return res