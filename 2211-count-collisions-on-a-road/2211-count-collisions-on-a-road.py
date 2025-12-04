class Solution:
    def countCollisions(self, directions: str) -> int:
        a = 0
        res = 0
        r = 0
        for d in directions:
            if d == 'R':
                r += 1
                a = 1
            elif d == 'L':
                res += r
                r = 0
                res += 1 if a else 0
            else:
                res += r
                r = 0
                a = 1
        return res