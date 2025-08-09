class Solution:
    def minimumWeight(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        # ans of s1,s2,d = (dist(s1,s2) + dist(s2,d) + dist(d,s1)) / 2
        # dist(a,b) = depth(a) + depth(b) - 2*depth(lca(a,b))
        # ans of s1,s2,d = depth(s1) + depth(s2) + depth(d) - depth(lca(s1,s2)) + depth(lca(s2,d)) - depth(lca(d,s1))
        # find LCA: Tarjan's off-line algorithm
        N = len(edges)+1
        adj = [[] for _ in range(N)]
        for a,b,w in edges:
            adj[a].append([b,w])
            adj[b].append([a,w])

        f = list(range(N))
        size = [1]*N
        def root(a):
            while a != f[a]:
                a,f[a] = f[a], f[f[a]]
            return a
        def union(a,b):
            a,b = root(a),root(b)
            if size[a] < size[b]:
                a,b = b,a
            f[b] = a
            size[a] += size[b]
            return a
        
        Q = [[] for _ in range(N)]
        for i, (a, b, c) in enumerate(queries):
            Q[a].append([b,c,i])
            Q[b].append([c,a,i])
            Q[c].append([a,b,i])

        vis = [0]*N
        ancestor = list(range(N))
        depth = [0]*N

        res = [0]*len(queries)

        def dfs(a):
            vis[a] = 1
            for b,c,i in Q[a]:
                res[i] += depth[a]
                if vis[b]:
                    res[i] -= depth[ancestor[root(b)]]
                if vis[c]:
                    res[i] -= depth[ancestor[root(c)]]
                    
            for b,w in adj[a]:
                if vis[b]: continue
                depth[b] = depth[a]+w
                dfs(b)
                ancestor[union(a,b)] = a
            
        dfs(0)
        return res