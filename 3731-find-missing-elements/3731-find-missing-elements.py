class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        S = set(nums)
        res = []
        for i in range(min(nums)+1, max(nums)):
            if i not in S:
                res.append(i)
        return res