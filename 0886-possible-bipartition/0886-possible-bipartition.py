class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for a,b in dislikes:
            adj[a].append(b)
            adj[b].append(a)
        vis = [0]*(n+1)
        vis[0] = 2
        
        def dfs(prev, cur, color):
            if vis[cur] > 0:
                return vis[cur] == color
            vis[cur] = 3 - vis[prev]
            if vis[cur] != color:
                return False
            res = True
            for ne in adj[cur]:
                res &= dfs(cur, ne, 3 - vis[cur])
            return res
        
        res = True
        for i in range(1,n+1):
            if vis[i] == 0:
                res &= dfs(0, i, 1)
        return res
            
        