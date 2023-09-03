class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        A = sorted([cnt for ch,cnt in Counter(s).items()], reverse=True)
        if len(A) < k:
            return 0
        bar = A[k-1]
        res = 1
        mod = 10**9+7
        no_bar = 0
        no_gt_bar = 0
        for n in A:
            if n > bar:
                res = (res*n) % mod
                no_gt_bar += 1
            elif n == bar:
                no_bar += 1
            else:
                break
        # print(A)
        # print(res, no_gt_bar, no_bar)
        return res * (bar**(k - no_gt_bar) * comb(no_bar, k - no_gt_bar)) % mod
        