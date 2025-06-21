class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        A = sorted(Counter(word).values())
        rsum = sum(A)
        lsum = 0
        N = len(A)
        i = j = 0
        res = inf

        for r in range(1, len(word)+1):
            while i < N and r >= A[i]:
                rsum -= A[i]
                i += 1
            l = r-k
            while j < N and A[j] < l:
                lsum += A[j]
                j += 1
            res = min(res, rsum - r*(N-i) + lsum)
        return res