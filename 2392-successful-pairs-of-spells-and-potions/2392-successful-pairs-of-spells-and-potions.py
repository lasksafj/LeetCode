class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        N = len(potions)
        res = []
        for s in spells:
            d = ceil(success/s)
            res.append(N - bisect_left(potions, d))
        return res