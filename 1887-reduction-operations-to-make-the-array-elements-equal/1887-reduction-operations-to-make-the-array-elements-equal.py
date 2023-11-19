class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        a = 1
        res = 0
        for i in range(len(nums)-2,-1,-1):
            if nums[i] != nums[i+1]:
                res += a
            a += 1
        return res
                