class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(mi):
            cur = 0
            res = 0
            for n in nums:
                if n > mi:
                    return False
                cur += n
                if cur > mi:
                    res += 1
                    cur = n
            return res <= k-1

        l,r = min(nums), sum(nums)
        while l < r:
            mi = (l+r)//2
            if check(mi):
                r = mi
            else:
                l = mi+1
        return l