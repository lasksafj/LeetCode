class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a,b,w in edges:
            adj[a].append([b,w])
            adj[b].append([a,w])
            
        distanceToLastNode = [inf]*(n+1)
        pq = [[0,n]]
        distanceToLastNode[n] = 0
        while pq:
            d,i = heappop(pq)
            if d > distanceToLastNode[i]:
                continue
            for ne,w in adj[i]:
                if distanceToLastNode[ne] > d+w:
                    distanceToLastNode[ne] = d+w
                    heappush(pq, (d+w,ne))
        
        @cache
        def dfs(i):
            if i == n:
                return 1
            res = 0
            for ne,w in adj[i]:
                if distanceToLastNode[ne] < distanceToLastNode[i]:
                    res += dfs(ne)
            return res
        return dfs(1) % (10**9+7)