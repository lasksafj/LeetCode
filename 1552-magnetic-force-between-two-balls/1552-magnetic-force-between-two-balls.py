class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def check(x):
            res = 1
            cur = position[0]
            for p in position[1:]:
                if p-cur >= x:
                    res += 1
                    cur = p
            return res >= m
        l,r = 0,10**9
        while l <= r:
            mi = (l+r)//2
            if check(mi):
                l = mi+1
            else:
                r = mi-1
        return r