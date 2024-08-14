class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        def check(mi):
            res = 0
            for i,b in enumerate(nums):
                res += max(0, i-bisect_left(nums, b-mi))
            return res >= k
        l,r = 0,nums[-1]-nums[0]
        while l <= r:
            mi = (l+r)//2
            if check(mi):
                r = mi-1
            else:
                l = mi+1
        return l