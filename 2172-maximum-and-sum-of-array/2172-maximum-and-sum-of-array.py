class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        @cache
        def dfs(i, mask):
            if i == len(nums):
                return 0
            res = 0
            for slot in range(1, numSlots+1):
                if (1<<((slot-1)*2)) & mask == 0:
                    res = max(res, dfs(i+1, (1<<((slot-1)*2)) | mask) + (nums[i] & slot))
                elif (1<<((slot-1)*2+1)) & mask == 0:
                    res = max(res, dfs(i+1, (1<<((slot-1)*2+1)) | mask) + (nums[i] & slot))
            return res
        res = dfs(0, 0)
        return res