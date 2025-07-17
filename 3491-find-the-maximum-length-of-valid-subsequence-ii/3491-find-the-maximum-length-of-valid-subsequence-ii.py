class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = {}
        for n in nums:
            ndp = {}
            for prev in list(dp.keys()):
                m = (n+prev)%k
                if n not in ndp:
                    ndp[n] = [1]*k
                ndp[n][m] = max(ndp[n][m], dp[prev][m] + 1)
            for prev in dp:
                if prev not in ndp:
                    ndp[prev] = dp[prev]
            if n not in ndp:
                ndp[n] = [1]*k
            dp = ndp
        return max(max(row) for row in dp.values())