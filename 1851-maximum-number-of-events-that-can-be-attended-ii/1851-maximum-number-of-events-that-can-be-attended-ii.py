class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda x:x[1])
        events = [[0,0,0]] + events
        N = len(events)
        dp = [0]*N
        for t in range(k):
            ndp = [0]*N
            for i in range(1, N):
                a,b,v = events[i]
                j = bisect_right(events, a-1, key=lambda x:x[1])-1
                ndp[i] = max(ndp[i-1], dp[j] + v)
            dp = ndp
        return dp[-1]