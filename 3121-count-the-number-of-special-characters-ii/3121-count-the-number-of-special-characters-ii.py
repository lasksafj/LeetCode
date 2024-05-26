class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        res = 0
        for ch in ascii_lowercase:
            first_upper = False
            first_lower = False
            ok = True
            for w in word:
                if w.lower() != ch:
                    continue
                if w.isupper():
                    first_upper = True
                elif first_upper:
                    ok = False
                    break
                else:
                    first_lower = True
            if ok and first_upper and first_lower:
                res += 1
        return res