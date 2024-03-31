class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        if minK > maxK:
            return 0
        j,mi,ma = -1,-1,-1
        res = 0
        for i,n in enumerate(nums):
            if n == minK:
                mi = i
            if n == maxK:
                ma = i
            if n > maxK or n < minK:
                j = i
            res += max(0, min(mi,ma) - j)
        return res