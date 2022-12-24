class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = [defaultdict(int) for _ in range(n+1)]
        for a,b,c in roads:
            adj[a][b] = c
            adj[b][a] = c
        res = inf
        q = deque([1])
        vis = set()
        while q:
            a = q.popleft()
            for ne in adj[a]:
                res = min(res, adj[a][ne])
                if ne not in vis:
                    q.append(ne)
                    vis.add(ne)
        return res