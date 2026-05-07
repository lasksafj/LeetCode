class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        Ma = [0]*len(nums)
        for i,n in enumerate(nums):
            Ma[i] = max(Ma[i-1], n)
        mi_r = inf
        cur = nums[-1]
        for i in range(len(nums)-1,-1,-1):
            ma_l = Ma[i]
            if ma_l > mi_r:
                res[i] = cur
            else:
                res[i] = ma_l
            if mi_r > nums[i]:
                mi_r = nums[i]
                cur = res[i]
        return res