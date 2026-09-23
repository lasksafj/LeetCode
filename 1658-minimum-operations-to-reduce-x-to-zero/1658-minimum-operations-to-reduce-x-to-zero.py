class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        j = 0
        s = 0
        res = inf
        t = sum(nums) - x
        for i in range(len(nums)):
            s += nums[i]
            while j <= i and s > t:
                s -= nums[j]
                j += 1
            if s == t:
                res = min(res, len(nums) - (i-j+1))
        return res if res < inf else -1