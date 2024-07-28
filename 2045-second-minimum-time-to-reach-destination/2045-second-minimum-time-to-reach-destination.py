class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        def sol(d):
            res = 0
            while d > 0:
                res += time
                d -= 1
                if d > 0 and res%(change*2) >= change:
                    res += 2*change - (res%(change*2))

            return res
        
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        vis = [inf]*(n+1)
        q = deque([1])
        d = 0
        triangle = 2
        while q and d <= vis[n]+1:
            d += 1
            for _ in range(len(q)):
                cur = q.popleft()
                for ne in adj[cur]:
                    if d > vis[ne] + 1:
                        continue
                    if ne == n and d > vis[ne]:
                        return sol(d)
                    vis[ne] = min(vis[ne], d)
                    q.append(ne)
                    
        return sol(vis[n]+2)