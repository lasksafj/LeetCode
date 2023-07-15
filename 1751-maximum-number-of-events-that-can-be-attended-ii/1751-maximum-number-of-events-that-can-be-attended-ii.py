class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        n = len(events)
        dp = [[-1] * n for _ in range(k + 1)]
        def dfs(i, k, prev_ending_time):
            if i == len(events) or k == 0:
                return 0
            if events[i][0] <= prev_ending_time:            
                return dfs(i + 1, k, prev_ending_time)
            if dp[k][i] != -1:
                return dp[k][i]
            res = max(dfs(i+1, k, prev_ending_time), dfs(i+1, k-1, events[i][1]) + events[i][2])
            dp[k][i] = res
            return res
        return dfs(0,k,-1)