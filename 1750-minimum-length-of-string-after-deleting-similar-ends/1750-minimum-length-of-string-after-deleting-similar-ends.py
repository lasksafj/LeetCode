class Solution:
    def minimumLength(self, s: str) -> int:
        i,j = 0, len(s)-1
        while i < j:
            if s[i] == s[j]:
                while i < j and s[i] == s[i+1]:
                    i += 1
                while i < j and s[j] == s[j-1]:
                    j -= 1
                i += 1
                j -= 1
            else:
                break
        return max(0, j-i+1)