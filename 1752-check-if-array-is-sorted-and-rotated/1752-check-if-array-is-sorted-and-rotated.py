class Solution:
    def check(self, nums: List[int]) -> bool:
        mi = inf
        ma = inf
        for a,b in zip(nums,nums[1:]):
            if a > b:
                if ma < inf: return False
                ma = a
                mi = nums[0]
            if not b <= mi: return False
        return True