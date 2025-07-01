class Solution:
    def possibleStringCount(self, word: str) -> int:
        N = len(word)
        i = 0
        res = 0
        while i < N:
            j = i+1
            while j < N and word[i] == word[j]:
                j += 1
            res += j-i-1
            i = j
        return res+1