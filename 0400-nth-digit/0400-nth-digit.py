class Solution:
    def findNthDigit(self, n: int) -> int:
        if n < 10:
            return n
        def count(mi):
            res = 0
            for d in range(10,0,-1):
                if mi//(10**d) > 0:
                    res += ((mi-(10**d))+1) * (d+1)
                    break
            d -= 1
            while d >= 0:
                res += 9*(10**d) * (d+1)
                d -= 1
            return res
                    
        l,r = 1,10**9
        while l <= r:
            mi = (l+r)//2
            if count(mi) < n:
                l = mi+1
            else:
                r = mi-1
        d = n-count(r)
        for ch in str(r+1):
            d -= 1
            if d == 0:
                return int(ch)
        return int(str(r+1)[-1])