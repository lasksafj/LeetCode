class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        ch1,ch2 = 'a','b'
        if x < y:
            ch1 = 'b'
            ch2 = 'a'
            x,y = y,x
        res = 0
        st = []
        a,b = 0,0
        for ch in s+'-':
            if ch == ch1:
                a += 1
            elif ch == ch2:
                if a > 0:
                    a -= 1
                    res += x
                else:
                    b += 1
            else:
                res += min(a,b) * y
                a,b = 0,0
        return res
                