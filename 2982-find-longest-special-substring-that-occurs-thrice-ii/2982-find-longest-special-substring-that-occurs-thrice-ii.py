class Solution:
    def maximumLength(self, s: str) -> int:
        N = len(s)
        l = 1
        grs = [[] for _ in range(26)]
        grs[ord(s[0])-ord('a')].append(1)
        for i in range(1,N):
            if s[i] == s[i-1]:
                l += 1
            else:
                l = 1
            grs[ord(s[i])-ord('a')].append(l)
        res = -1
        for gr in grs:
            if len(gr) >= 3:
                res = max(res, sorted(gr)[-3])
        return res