class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        # a,b ---- c,d
        # reverse <=> a,c ---- b,d
        # diff = abs(a-c) + abs(b-d) - ( abs(a-b) + abs(c-d) )
        # best situation when [min(a,b),max(a,b)] not intersect with [min(c,d),max(c,d)]
        # diff = (min(c,d) - max(a,b)) * 2
        
        ma = inf
        mi = -inf
        res = -inf
        total = 0
        for a,b in zip(nums, nums[1:]):
            total += abs(a-b)
            res = max(res, max((min(a,b)-ma)*2, (mi-max(a,b))*2 ) )
            ma = min(ma, max(a,b))
            mi = max(mi, min(a,b))
            
            # reverse [...a] or [b...]
            res = max(res, -abs(a-b)+abs(nums[0]-b), -abs(a-b)+abs(a-nums[-1]))
        return res + total