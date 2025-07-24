class Solution:
    def maxScore(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        A = [0]*n
        q = deque()
        for a in adj:
            if len(adj[a]) < 2:
                q.append(a)
        if not q:
            q.append(0)
        vis = set(q)
        d = 1
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                A[cur] = d
                d += 1
                for ne in adj[cur]:
                    if ne not in vis:
                        q.append(ne)
                        vis.add(ne)
        return sum(A[a]*A[b] for a,b in edges)