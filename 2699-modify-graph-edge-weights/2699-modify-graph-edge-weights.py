class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        adj = [[0]*n for _ in range(n)]
        for a,b,w in edges:
            adj[a][b] = w
            adj[b][a] = w
        pq = [(0,source)]
        dist = [inf]*n
        dist[source] = 0
        while pq:
            d, cur = heappop(pq)
            for ne in range(n):
                w = adj[cur][ne]
                if w == 0:
                    continue
                if w > -1 and dist[ne] > d+w:
                    dist[ne] = d+w
                    heappush(pq, (d+w, ne))
        if dist[destination] < target:
            return []
        if dist[destination] == target:
            return [[a,b,(w if w > -1 else 2000000000)] for a,b,w in edges]
            
        pq = [(0,source)]
        vis = [(inf,-1)]*n
        vis[source] = (0,source)
        while pq:
            d, cur = heappop(pq)
            for ne in range(n):
                w = adj[cur][ne]
                if w == 0:
                    continue
                w = max(w,1)
                if vis[ne][0] > d+w:
                    vis[ne] = (d+w,cur)
                    heappush(pq, (d+w, ne))
        if vis[destination][0] > target:
            return []
        cur = destination
        while vis[cur][1] != cur:
            prev = vis[cur][1]
            if adj[prev][cur] == -1:
                if dist[prev] < target:
                    adj[prev][cur] = target - dist[prev]
                    adj[cur][prev] = target - dist[prev]
                    break
                adj[prev][cur] = 1
                adj[cur][prev] = 1
            target -= adj[prev][cur]
            cur = prev
            
        res = []
        for a,b,w in edges:
            if adj[a][b] == -1:
                res.append([a,b,2000000000])
            else:
                res.append([a,b,adj[a][b]])
        
        return res