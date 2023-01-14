class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        def f(x):
            if x == p[x]:
                return x
            return f(p[x])
        def join(a,b):
            y1,y2 = f(a), f(b)
            if y1 < y2:
                p[y2] = y1
            elif y1 > y2:
                p[y1] = y2
        
        p = {}
        for c in ascii_lowercase:
            p[c] = c
        for i in range(len(s1)):
            join(s1[i], s2[i])
            
        # print(p)
        res = ''
        for c in baseStr:
            res += f(c)
        return res