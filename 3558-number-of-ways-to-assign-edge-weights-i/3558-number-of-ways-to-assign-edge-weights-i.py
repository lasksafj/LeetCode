class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        def dfs(i,prev):
            res = 0
            for ne in adj[i]:
                if ne != prev:
                    res = max(res, dfs(ne, i)+1)
            return res
        d = dfs(1,0)
        return pow(2,d-1,10**9+7)