class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # dp[n]: min prefix sum cnt[n] - cnt[k]
        dp = defaultdict(lambda:inf)
        cnt = defaultdict(int)
        res = 0
        for n in nums:
            cnt[n] += 1
            if n != k:
                cur = cnt[n] - cnt[k]
                dp[n] = min(dp[n], cur-1)
                res = max(res, cur - dp[n])
        return res + cnt[k]