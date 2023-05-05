class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        a = 0
        for i in range(k):
            if s[i] in 'aeiou':
                a += 1
        res = a
        for i in range(k, n):
            if s[i-k] in 'aeiou':
                a -= 1
            if s[i] in 'aeiou':
                a += 1
            res = max(res,a)
        return res