class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a,b,c in roads:
            adj[a].append([b,c])
            adj[b].append([a,c])
        pq = [[100000, 1]]
        vis = [1000001]*(n+1)
        while pq:
            v,c = heappop(pq)
            for ne,d in adj[c]:
                d = min(d,v)
                if vis[ne] > d:
                    vis[ne] = d
                    heappush(pq, [d,ne])
        return vis[n]