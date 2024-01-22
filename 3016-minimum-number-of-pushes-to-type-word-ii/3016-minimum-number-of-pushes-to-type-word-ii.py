class Solution:
    def minimumPushes(self, word: str) -> int:
        A = sorted(Counter(word).values(), reverse=True)
        res = 0
        for i,n in enumerate(A):
            res += n*((i+8)//8)
        return res