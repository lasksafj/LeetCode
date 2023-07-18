class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        @cache
        def dfs(i,t):
            if t >= len(cost):
                return 0
            if i == len(cost):
                return inf
            return min(dfs(i+1,t), dfs(i+1, t+time[i]+1) + cost[i])
        return dfs(0,0)