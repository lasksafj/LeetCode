class Solution:
    def isValid(self, word: str) -> bool:
        v = co = 0
        for c in word:
            if not c.isalnum(): return False
            if c in 'aeiouAEIOU': v += 1
            elif not c.isdigit(): co += 1
        return len(word) >= 3 and v>0 and co>0