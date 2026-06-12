class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        n = len(edges)+1
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        D = [0]*(n+1)
        L = int(log2(n))+2
        up = [[0]*L for _ in range(n+1)]
        def dfs(i,prev,d):
            D[i] = d
            up[i][0] = prev
            for ne in adj[i]:
                if ne != prev:
                    dfs(ne, i, d+1)
        dfs(1,0, 0)
        for k in range(1, L):
            for i in range(1, n+1):
                up[i][k] = up[up[i][k-1]][k-1]
        def lca(a,b):
            if a == b: return a
            if D[a] < D[b]: a,b = b,a
            for k in range(L-1,-1,-1):
                if D[up[a][k]] >= D[b]:
                    a = up[a][k]
            if a == b: return a
            for k in range(L-1,-1,-1):
                if up[a][k] != up[b][k]:
                    a,b = up[a][k], up[b][k]
            return up[a][0]

        MOD = 10**9+7
        res = []
        for a,b in queries:
            d = D[a] + D[b] - D[lca(a,b)] * 2
            if d == 0:
                res.append(0)
            else:
                res.append(pow(2,d-1,MOD))
        return res