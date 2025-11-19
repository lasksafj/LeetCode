class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        S = set(nums)
        while original in S:
            original *= 2
        return original