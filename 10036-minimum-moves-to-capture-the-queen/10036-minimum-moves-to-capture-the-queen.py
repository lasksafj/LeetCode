class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        res = 2
        if a == e:
            if c == a:
                mi,ma = min(b,f),max(b,f)
                if mi < d < ma:
                    res = 2
                else:
                    return 1
            else:
                return 1
        elif b == f:
            if d == b:
                mi,ma = min(a,e),max(a,e)
                if mi < c < ma:
                    res = 2
                else:
                    return 1
            else:
                return 1
        
        if c-d == e-f or c+d==e+f:
            if a-b == c-d or a+b==c+d:
                mi,ma = min(c,e),max(c,e)
                if mi < a < ma:
                    res = 2
                else:
                    return 1
            else:
                return 1
        return res