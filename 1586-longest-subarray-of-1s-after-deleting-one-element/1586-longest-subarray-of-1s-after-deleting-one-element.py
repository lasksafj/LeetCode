class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        s = set(nums)
        if len(s) == 1:
            return len(nums)-1 if nums[0] == 1 else 0
        res = 0
        mp = [0]*2
        j = 0
        for i,n in enumerate(nums):
            mp[n] += 1
            while mp[0] > 1:
                mp[nums[j]] -= 1
                j += 1
            res = max(res, i-j+1)
        return res-1