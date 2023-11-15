class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if k > sum(candies):
            return 0
        
        def check(x):
            res = 0
            for n in candies:
                res += n//x
                if res >= k:
                    return True
            return False
        l,r = 1,sum(candies)+1
        while l < r:
            mi = (l+r)//2
            if check(mi):
                l = mi+1
            else:
                r = mi
        return r-1