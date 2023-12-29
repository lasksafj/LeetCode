class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        N = len(nums)
        pre = [0]*(N+1)
        for i in range(N):
            pre[i+1] = pre[i] + nums[i]
        for i in range(N-1,-1,-1):
            n = nums[i]
            if pre[i] > n:
                return pre[i]+n
        return -1