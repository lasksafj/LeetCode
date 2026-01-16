class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target: return 0
        pref = list(accumulate(nums, initial=0))
        def check(mi):
            for i in range(len(nums)-mi+1):
                j = i+mi
                if pref[j] - pref[i] >= target:
                    return True
            return False
        l,r = 1,len(nums)
        while l < r:
            mi = (l+r)//2
            if check(mi):
                r = mi
            else:
                l = mi+1
        return l