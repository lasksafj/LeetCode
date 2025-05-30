class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        return sorted([n&1 for n in nums])