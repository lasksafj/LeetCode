class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        mi = inf
        res = -inf
        for n in nums:
            res = max(res, n-mi)
            mi = min(mi, n)
        return res if res > 0 else -1