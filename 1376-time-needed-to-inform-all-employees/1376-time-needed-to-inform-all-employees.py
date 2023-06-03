class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj = defaultdict(list)
        for i,m in enumerate(manager):
            adj[m].append(i)
        def dfs(prev, cur):
            res = 0
            for ne in adj[cur]:
                if ne != prev:
                    res = max(res, dfs(cur, ne))
            return res + informTime[cur]
        return dfs(-1, headID)