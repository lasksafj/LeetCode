class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay)//k < m:
            return -1
        def check(x):
            res = 0
            cnt = 0
            for d in bloomDay:
                if d <= x:
                    cnt += 1
                else:
                    cnt = 0
                if cnt == k:
                    res += 1
                    cnt = 0
            return res >= m
        l,r = 0,max(bloomDay)
        while l <= r:
            mi = (l+r)//2
            if check(mi):
                r = mi-1
            else:
                l = mi+1
        return l
                