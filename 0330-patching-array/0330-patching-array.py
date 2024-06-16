class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        res = int(nums[0] > 1)
        k = 1
        i = int(nums[0] == 1)
        while k < n:
            if i < len(nums) and nums[i] <= k+1:
                k += nums[i]
                i += 1
            else:
                res += 1
                k += k+1
        return res