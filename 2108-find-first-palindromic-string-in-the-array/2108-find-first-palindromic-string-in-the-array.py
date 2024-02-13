def check(s):
    i,j = 0,len(s)-1
    while i < j and s[i] == s[j]:
        i += 1
        j -= 1
    return i >= j

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for w in words:
            if check(w):
                return w
        return ''