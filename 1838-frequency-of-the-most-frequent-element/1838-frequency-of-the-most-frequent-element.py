class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0
        s = 0
        j = 0
        for i in range(len(nums)):
            s += nums[i]
            while (i-j+1) * nums[i] - s > k:
                s -= nums[j]
                j += 1
            res = max(res, i-j+1)
        return res