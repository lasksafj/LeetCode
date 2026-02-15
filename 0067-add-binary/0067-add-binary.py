class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]
        res = []
        c = 0
        i = j = 0
        while i < len(a) or j < len(b) or c:
            d = (int(a[i]) if i < len(a) else 0) + (int(b[j]) if j < len(b) else 0) + c
            res.append(str(d%2))
            c = d//2
            i += 1
            j += 1
        return (''.join(res) + a[i:] + b[j:])[::-1]