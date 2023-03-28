class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        days.sort()
        @cache
        def dfs(i):
            if i == len(days):
                return 0
            return min( costs[0] + dfs(i+1),
                        costs[1] + dfs(bisect_left(days, days[i]+7)),
                        costs[2] + dfs(bisect_left(days, days[i]+30)) )
        return dfs(0)