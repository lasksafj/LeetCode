class Solution:
    def maxConsecutiveAnswers(self, A: str, k: int) -> int:
        res = 0
        j = 0
        freq = defaultdict(int)
        ma = 0
        for i in range(len(A)):
            freq[A[i]] += 1
            ma = max(ma, freq[A[i]])
            if ma+k < i-j+1:
                freq[A[j]] -= 1
                j += 1
            res = max(res, i-j+1)
        return res