class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res += min(n%3, 3-n%3)
        return res