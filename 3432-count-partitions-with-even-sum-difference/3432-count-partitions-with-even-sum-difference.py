class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        s = sum(nums)
        res = 0
        l = 0
        for n in nums[:-1]:
            l += n
            s -= n
            res += abs(s-l)&1 == 0
        return res