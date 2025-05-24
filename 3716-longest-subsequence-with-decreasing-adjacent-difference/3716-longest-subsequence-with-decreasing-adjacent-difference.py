from typing import List

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n

        # Constraints say nums[i] <= 300
        MAXV = 300
        MAXD = 300

        # best_suf[v][d] = best length of a subsequence ending with value v
        # whose last absolute-difference was >= d
        best_suf = [[0] * (MAXD + 1) for _ in range(MAXV + 1)]

        # Initialize with the first element
        ans = 1
        suf = [1] * (MAXD + 1)
        for d in range(MAXD - 1, -1, -1):
            suf[d] = max(suf[d], suf[d + 1])
        v0 = nums[0]
        for d in range(MAXD + 1):
            best_suf[v0][d] = suf[d]

        # Process the rest of the array
        for j in range(1, n):
            dp = [1] * (MAXD + 1)   # dp[d] = best subseq ending at j with last-diff = d

            # Try to append nums[j] after any previous value v
            x = nums[j]
            for v in range(1, MAXV + 1):
                delta = abs(x - v)
                prev_best = best_suf[v][delta]
                if prev_best > 0:
                    dp[delta] = max(dp[delta], prev_best + 1)

            # Build suffix-maximum of dp so that suf[d] = max(dp[e] for e >= d)
            suf[MAXD] = dp[MAXD]
            for d in range(MAXD - 1, -1, -1):
                suf[d] = max(dp[d], suf[d + 1])

            # Update best_suf for value = nums[j]
            for d in range(MAXD + 1):
                best_suf[x][d] = max(best_suf[x][d], suf[d])

            # Update global answer
            ans = max(ans, max(dp))

        return ans
