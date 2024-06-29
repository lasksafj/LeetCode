class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj = defaultdict(list)
        for a,b in edges:
            adj[b].append(a)
        @cache
        def dfs(i):
            res = []
            for ne in adj[i]:
                res += dfs(ne)
            return [i] + sorted(list(set(res)))
        res = []
        for i in range(n):
            res.append(dfs(i)[1:])
        return res