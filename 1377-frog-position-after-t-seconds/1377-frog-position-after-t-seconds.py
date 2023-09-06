class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        if n == 1:
            return 1
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        adj[1].append(0)
        q = deque([[1,1]])
        vis = set()
        vis.add(0)
        while q and t >= 0:
            for _ in range(len(q)):
                v,p = q.popleft()
                if v == target:
                    return p if t == 0 or len(adj[v]) == 1 else 0
                if len(adj[v]) == 1:
                    if v == target:
                        return p
                    continue
                np = p / (len(adj[v]) - 1) if v != -1 else 1
                for ne in adj[v]:
                    if ne not in vis:
                        q.append([ne, np])
                        vis.add(ne)
            t -= 1
        return 0