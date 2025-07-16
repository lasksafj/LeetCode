class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        A = [n%2 for n in nums]
        res = max(Counter(A).values())
        dp0 = dp1 = 0
        for a in A:
            if a&1:
                dp1 = max(dp1, dp0 + 1)
            else:
                dp0 = max(dp0, dp1 + 1)
        return max(dp0, dp1, res)