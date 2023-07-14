class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int)
        res = 0
        for i,n in enumerate(arr):
            dp[n] = dp[n-difference] + 1
            res = max(res, dp[n])
        return res