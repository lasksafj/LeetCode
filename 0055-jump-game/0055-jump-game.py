class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        ma = 0
        for i in range(n-1):
            if i > ma:
                return False
            ma = max(ma, i+nums[i])
            if ma >= n-1:
                return True
        return False