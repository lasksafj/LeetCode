def dist(a,b):
    a,b = ord(a)-ord('a'),ord(b)-ord('a')
    if b < a:
        a,b = b,a
    return min(b-a, 26-b+a)

class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        res = []
        for ch in s:
            if k == 0:
                res.append(ch)
                continue
            for c in ascii_lowercase:
                d = dist(c,ch)
                # print(c,ch,d)
                if k >= d:
                    res.append(c)
                    k -= d
                    break
        return ''.join(res)