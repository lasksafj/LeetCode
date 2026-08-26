class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums.sort()
        d = 1
        for n in nums:
            if k*d < n:
                return k*d
            elif k*d == n:
                d += 1
        return k*d