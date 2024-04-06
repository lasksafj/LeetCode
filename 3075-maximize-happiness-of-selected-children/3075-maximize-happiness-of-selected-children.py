class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        N = len(happiness)
        res = 0
        for i in range(N-k, N):
            res += max(0, happiness[i]-k+1)
            k -= 1
        return res