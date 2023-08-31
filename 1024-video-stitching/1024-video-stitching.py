class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort()
        dp = [inf]*(time+1)
        dp[0] = 0
        for a,b in clips:
            b = min(time,b)
            for j in range(a, b+1):
                dp[b] = min(dp[b], dp[j] + 1)
        return dp[time] if dp[time] < inf else -1