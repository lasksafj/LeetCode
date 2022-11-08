class Solution:
    def appealSum(self, s: str) -> int:
        occur_pos = {}
        for c in string.ascii_lowercase:
            occur_pos[c] = -1
        prev = [0] * len(s)
        dp = [0] * len(s)
        for i in range(len(s)):
            prev[i] = (prev[i-1] if i>0 else 0) + (i - occur_pos[s[i]])
            dp[i] = (dp[i-1] if i>0 else 0) + prev[i]
            occur_pos[s[i]] = i
        return dp[len(s)-1]