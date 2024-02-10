class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for mi in range(len(s)):
            i,j = mi,mi
            while i>=0 and j<len(s):
                if s[i]==s[j]:
                    res += 1
                else:
                    break
                i-=1
                j+=1
            i,j = mi,mi+1
            while i>=0 and j<len(s):
                if s[i]==s[j]:
                    res += 1
                else:
                    break
                i-=1
                j+=1
        return res