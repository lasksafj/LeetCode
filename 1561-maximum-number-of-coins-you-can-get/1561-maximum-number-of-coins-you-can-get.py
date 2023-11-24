class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        res = 0
        n = 0
        for i in range(len(piles)-2,-1,-2):
            n += 3
            res += piles[i]
            if n == len(piles):
                break
        return res