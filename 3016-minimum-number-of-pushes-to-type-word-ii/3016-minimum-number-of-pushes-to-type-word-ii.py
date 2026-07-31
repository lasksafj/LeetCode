class Solution:
    def minimumPushes(self, word: str) -> int:
        res = 0
        for i,v in enumerate(sorted(Counter(word).values(), reverse=True)):
            res += (i//8 + 1)*v
        return res