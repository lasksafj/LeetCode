class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        f = {c:c for c in ascii_lowercase}
        def root(c):
            if c != f[c]:
                f[c] = root(f[c])
            return f[c]
        
        def union(a,b):
            a = root(a)
            b = root(b)
            if a < b:
                f[b] = a
            else:
                f[a] = b

        for a,b in zip(s1,s2):
            union(a,b)
        res = ''
        for c in baseStr:
            res += root(c)
        return res