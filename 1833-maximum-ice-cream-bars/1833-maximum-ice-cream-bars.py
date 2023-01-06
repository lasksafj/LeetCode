class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        res = 0
        for c in sorted(costs):
            coins -= c
            if coins >= 0:
                res += 1
            else:
                return res
        return res