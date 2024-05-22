class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        A = sorted(Counter(word).values())
        cnt = Counter(A)
        i = 0
        cur = 0
        res = inf
        while i < len(A):
            mi = A[i]
            ma = mi+k
            j = len(A)-1
            d = cur
            while j >= 0 and A[j] > ma:
                d += A[j]-ma
                j -= 1
            res = min(res, d)
            i += cnt[mi]
            cur += mi*cnt[mi]
        return res
        