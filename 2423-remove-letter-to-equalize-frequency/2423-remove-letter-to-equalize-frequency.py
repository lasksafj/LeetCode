class Solution:
    def equalFrequency(self, word: str) -> bool:
        A = list(Counter(word).values())
        for i in range(len(A)):
            A[i] -= 1
            l = len(A) - (A[i] == 0)
            if sum(A)/l == max(A):
                return True
            A[i] += 1
        return False