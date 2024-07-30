class Solution:
    def minimumDeletions(self, s: str) -> int:
        N = len(s)
        dp = 0
        b_cnt = 0
        for i,ch in enumerate(s):
            if ch == 'b':
                # dp[i + 1] = dp[i]
                b_cnt += 1
            else:
                # dp[i + 1] = min(dp[i] + 1, b_count)
                dp = min(dp + 1, b_cnt)
        return dp