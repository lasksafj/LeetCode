class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        from itertools import permutations
        cuboids = [sorted(cuboids[i]) for i in range(len(cuboids))]
        cuboids.sort()
        dp = [c[2] for c in cuboids]
        for i in range(len(cuboids)):
            w,l,h = cuboids[i]
            for j in range(i):
                pw,pl,ph = cuboids[j]
                if pw <= w and pl <= l and ph <= h:
                    dp[i] = max(dp[i], dp[j] + h)
        return max(dp)
                