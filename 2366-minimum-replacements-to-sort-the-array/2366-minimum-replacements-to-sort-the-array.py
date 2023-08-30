class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        r = nums[-1]
        res = 0
        for i in range(len(nums)-2,-1,-1):
            if nums[i] > r:
                if nums[i] % r == 0:
                    res += nums[i]//r - 1
                else:
                    d = nums[i]//r
                    res += d
                    r = max((nums[i] - r*(d-1))//2, nums[i]//(d+1))
            else:
                r = nums[i]
        return res
                    