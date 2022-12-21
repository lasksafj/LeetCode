class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for a,b in dislikes:
            adj[a].append(b)
            adj[b].append(a)
        
        parent = [i for i in range(n+1)]
        def root(x):
            if parent[x] == x:
                return x
            return root(parent[x])
        
        def union(x,y):
            xr,yr = root(x),root(y)
            if xr == yr:
                return False
            parent[y] = xr
        
        
        for i in range(1,n+1):
            for ne in adj[i]:
                if root(i) == root(ne):
                    return False
                union(adj[i][0], ne)
        return True
            
        