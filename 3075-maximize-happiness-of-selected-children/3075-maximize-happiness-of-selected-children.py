class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        d = 0
        res = 0
        for h in sorted(happiness)[::-1][:k]:
            res += max(0, h-d)
            d += 1
        return res