class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        brokenLetters = set(brokenLetters)
        res = 0
        for w in text.split():
            if any(c in brokenLetters for c in w):
                continue
            res += 1
        return res