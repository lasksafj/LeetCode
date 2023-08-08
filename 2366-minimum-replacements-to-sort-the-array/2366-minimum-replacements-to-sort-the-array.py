class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        N = len(nums)
        d = nums[-1]
        res = 0
        for i in range(N-2,-1,-1):
            if nums[i] > d:
                if nums[i]%d == 0:
                    res += nums[i]//d - 1
                else:
                    res += nums[i]//d
                    d = nums[i] // (nums[i]//d+1)
            else:
                d = nums[i]
        return res