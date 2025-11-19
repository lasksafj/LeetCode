class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        mask = 0
        for n in nums:
            if n%original != 0: continue
            d = n//original
            if d&(d-1) == 0:
                mask |= d
        mask = ~mask
        return original * (mask&(-mask))