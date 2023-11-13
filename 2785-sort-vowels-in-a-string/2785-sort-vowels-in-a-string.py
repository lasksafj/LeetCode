class Solution:
    def sortVowels(self, s: str) -> str:
        res = []
        A = defaultdict(int)
        sortedVowel = 'AEIOUaeiou'
        for c in s:
            if c not in sortedVowel:
                res.append(c)
            else:
                res.append(' ')
                A[c] += 1
        
        j = 0
        for i,c in enumerate(res):
            if c == ' ':
                while A[sortedVowel[j]] == 0:
                    j += 1
                res[i] = sortedVowel[j]
                A[sortedVowel[j]] -= 1
        return ''.join(res)