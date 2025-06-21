class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        A = sorted(Counter(word).values())
        rsum = sum(A)
        lsum = 0
        N = len(A)
        i = j = 0
        res = inf

        for i in range(N):
            while j < N and A[i] + k >= A[j]:
                rsum -= A[j]
                j += 1
            res = min(res, lsum + rsum - (A[i]+k)*(N-j))
            lsum += A[i]
        return res