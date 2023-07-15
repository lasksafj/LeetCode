class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        @cache
        def dfs(i, k):
            if i == len(events) or k == 0:
                return 0
            j = bisect_right(events, [events[i][1], inf, inf])
            res = max(dfs(i+1, k), dfs(j, k-1) + events[i][2])
            return res
        return dfs(0,k)