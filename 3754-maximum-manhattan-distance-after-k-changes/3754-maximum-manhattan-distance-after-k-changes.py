class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        res = 0
        up = 0
        right = 0
        no_l = no_r = 0
        no_d = no_u = 0
        for c in s:
            if c == 'S':
                no_d += 1
                up -= 1
            elif c == 'N':
                no_u += 1
                up += 1
            elif c == 'W':
                no_l += 1
                right -= 1
            else:
                no_r += 1
                right += 1
            res = max(res, abs(up) + abs(right) + min(k, min(no_u, no_d) + min(no_l, no_r)) * 2 )
        return res