class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        i = 0
        res = 0
        while i < len(word)-1:
            if abs(ord(word[i]) - ord(word[i+1])) <= 1:
                res += 1
                i += 2
            else:
                i += 1
        return res