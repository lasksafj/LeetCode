class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        adj = defaultdict(list)
        for a,b,c in edges:
            adj[a].append([b,c])
            adj[b].append([a,c])
        n = len(passingFees)
        @cache
        def dfs(cur, t):
            if t > maxTime:
                return inf
            if cur == n-1:
                return 0
            res = inf
            for ne,d in adj[cur]:
                res = min(res, dfs(ne, t+d) + passingFees[ne])
            return res
        res = dfs(0, 0)
        return res+passingFees[0] if res < inf else -1