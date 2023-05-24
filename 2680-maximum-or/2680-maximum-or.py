class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        res = 0
        pre = [0]*len(nums)
        pre[0] = nums[0]
        for i in range(1, len(nums)):
            pre[i] = pre[i-1] | nums[i]
        prev = 0
        for i in range(len(nums)-1,-1,-1):
            res = max(res, (nums[i]<<k) | (pre[i-1] if i>0 else 0) | prev)
            prev |= nums[i]
        return res