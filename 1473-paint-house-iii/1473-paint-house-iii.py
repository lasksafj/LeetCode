class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        @cache
        def dfs(cur, prev_color, target):
            if cur == m:
                if target == 0:
                    return 0
                return inf
            if target < 0:
                return inf
            if houses[cur] > 0:
                return dfs(cur+1, houses[cur], target - (houses[cur] != prev_color))
            res = inf
            for i in range(n):
                res = min(res, cost[cur][i] + dfs(cur+1, i+1, target - (i+1 != prev_color)))
            return res
        res = dfs(0, -1, target)
        return res if res < inf else -1