class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay)//k < m:
            return -1
        def check(x):
            res = 0
            i = 0
            while i < len(bloomDay):
                j = i
                while j < len(bloomDay) and bloomDay[j] <= x:
                    j += 1
                res += (j-i)//k
                i = max(j,j+1)
            return res >= m
        l,r = 0,max(bloomDay)
        while l <= r:
            mi = (l+r)//2
            if check(mi):
                r = mi-1
            else:
                l = mi+1
        return l
                