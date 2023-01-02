class Solution:
    def detectCapitalUse(self, w: str) -> bool:
        if w[0].isupper():
            return w[1:].islower() or w.isupper()
        return w.islower()