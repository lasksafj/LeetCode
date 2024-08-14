class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        N = len(nums)
        nums.sort()
        def check(mi):
            res = 0
            s = 0
            j = 0
            for i,b in enumerate(nums):
                while b-nums[j] > mi:
                    j += 1
                res += i-j
            return res >= k
        l,r = 0,nums[-1]-nums[0]
        while l <= r:
            mi = (l+r)//2
            if check(mi):
                r = mi-1
            else:
                l = mi+1
        return l