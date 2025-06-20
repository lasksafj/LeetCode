class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        l,r,u,d = 0,0,0,0
        x,y = 0,0
        res = 0
        for c in s:
            if c == 'W':
                x -= 1
                l += 1
            elif c == 'E':
                x += 1
                r += 1
            elif c == 'N':
                y += 1
                u += 1
            else:
                y -= 1
                d += 1
            res = max(res, abs(x) + abs(y) + min(k, min(l,r) + min(u,d))*2)
        return res