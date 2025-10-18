class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        A = [ord(c)-97 for c in s]
        @cache
        def dfs(i, mask, change):
            if i == len(s):
                return mask > 0
            nmask = mask|(1<<A[i])
            p = 0
            if bin(nmask).count('1') > k:
                nmask = 1<<A[i]
                p = 1
            res = dfs(i+1, nmask, change) + p
            if change == 0:
                return res
            for c in range(26):
                if c == A[i]: continue
                nmask = mask|(1<<c)
                p = 0
                if bin(nmask).count('1') > k:
                    nmask = 1<<c
                    p = 1
                res = max(res, dfs(i+1, nmask, change-1) + p)
            return res
        return dfs(0, 0, 1)