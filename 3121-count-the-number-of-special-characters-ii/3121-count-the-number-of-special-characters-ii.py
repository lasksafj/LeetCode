class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        res = 0
        for ch,upch in zip(ascii_lowercase, ascii_uppercase):
            res += ch in word and word.rfind(ch) < word.find(upch)
        return res