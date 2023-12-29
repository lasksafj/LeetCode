class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        N = len(nums)
        s = sum(nums)
        cur = 0
        for i in range(N-1,-1,-1):
            n = nums[i]
            cur += n
            if s-cur > n:
                return s-cur+n
        return -1