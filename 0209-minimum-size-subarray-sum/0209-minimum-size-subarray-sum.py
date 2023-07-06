class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s,j,res = 0,0,inf
        for i in range(len(nums)):
            s += nums[i]
            while j < i and s - nums[j] >= target:
                s -= nums[j]
                j += 1
            if s >= target:
                res = min(res, i-j+1)
        return res if res < inf else 0