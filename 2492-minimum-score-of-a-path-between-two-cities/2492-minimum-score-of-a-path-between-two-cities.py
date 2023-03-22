class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a,b,c in roads:
            adj[a].append([b,c])
            adj[b].append([a,c])
        vis = set()
        q = deque([1])
        res = 100001
        while q:
            c = q.popleft()
            for ne,d in adj[c]:
                res = min(res, d)
                if ne not in vis:
                    q.append(ne)
                    vis.add(ne)
        return res