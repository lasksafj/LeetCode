class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for a,b in dislikes:
            adj[a].append(b)
            adj[b].append(a)
        vis = [0]*(n+1)
        
        def dfs(cur, color):
            vis[cur] = color
            for ne in adj[cur]:
                if vis[ne] == color:
                    return False
                elif vis[ne] == 0 and not dfs(ne, 3 - vis[cur]):
                    return False
            return True
        
        for i in range(1,n+1):
            if vis[i] == 0 and not dfs(i, 1):
                return False
        return True
            
        