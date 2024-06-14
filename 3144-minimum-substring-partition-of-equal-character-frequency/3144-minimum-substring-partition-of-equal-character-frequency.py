class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        dp = [0] + [inf]*len(s)
        for i in range(len(s)):
            mp = defaultdict(int)
            ma = -inf
            mi = inf
            for j in range(i,-1,-1):
                mp[s[j]] += 1
                ma = max(ma, mp[s[j]])
                mi = min(mp.values())
                if ma == mi:
                    dp[i+1] = min(dp[i+1], dp[j] + 1)
        return dp[-1]