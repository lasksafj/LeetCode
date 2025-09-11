class Solution:
    def sortVowels(self, s: str) -> str:
        A = sorted([ch for ch in s if ch in 'euoaiEUOAI'],reverse=True)
        res = ''
        for ch in s:
            if ch in 'euoaiEUOAI':
                res += A.pop()
            else:
                res += ch
        return res