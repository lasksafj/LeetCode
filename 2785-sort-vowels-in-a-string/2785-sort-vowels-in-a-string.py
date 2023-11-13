class Solution:
    def sortVowels(self, s: str) -> str:
        res = []
        A = []
        for c in s:
            if c not in 'euoaiEUOAI':
                res.append(c)
            else:
                res.append(' ')
                A.append(c)
        A.sort()
        j = 0
        for i,c in enumerate(res):
            if c == ' ':
                res[i] = A[j]
                j += 1
        return ''.join(res)