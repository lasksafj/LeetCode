class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        res = 0
        i = 0
        for a in g:
            while i < len(s) and s[i] < a:
                i += 1
            if i == len(s):
                break
            res += 1
            i += 1
        return res