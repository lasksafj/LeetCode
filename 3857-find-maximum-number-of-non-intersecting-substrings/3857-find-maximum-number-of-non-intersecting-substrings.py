class Solution:
    def maxSubstrings(self, word: str) -> int:
        N = len(word)+1
        dp = [0]*N
        mp = defaultdict(list)
        for i in range(1,N):
            w = word[i-1]
            dp[i] = dp[i-1]
            j = len(mp[w])-1
            while j >= 0 and i - mp[w][j] < 3:
                j -= 1
            mp[w].append(i)
            if j < 0: continue
            dp[i] = max(dp[i], dp[mp[w][j]-1] + 1)
        return dp[-1]