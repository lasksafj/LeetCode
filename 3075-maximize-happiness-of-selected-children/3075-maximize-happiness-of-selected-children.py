class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        A = sorted(happiness)[::-1]
        res = 0
        d = 0
        for i in range(k):
            res += max(0, A[i] - d)
            d += 1
        return res