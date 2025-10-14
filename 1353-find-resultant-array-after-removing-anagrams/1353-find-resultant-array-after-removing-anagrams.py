class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        A = [sorted(w) for w in words]
        i = 0
        N = len(words)
        res = []
        while i < N:
            res.append(words[i])
            j = i+1
            while j < N and A[i] == A[j]:
                j += 1
            i = j
        return res