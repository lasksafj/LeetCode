class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for [a,b],v in zip(equations,values):
            adj[a].append((b,v))
            adj[b].append((a,1/v))
        def sol(a,b):
            q = deque([(a,1)])
            vis = set()
            vis.add(a)
            while q:
                c,k = q.popleft()
                for ne,v in adj[c]:
                    if ne == b:
                        return k*v
                    if ne not in vis:
                        q.append((ne,k*v))
                        vis.add(ne)
            return -1
        res = []
        for a,b in queries:
            if a == b:
                if a not in adj:
                    res.append(-1)
                else:
                    res.append(1)
            else:
                res.append(sol(a,b))
        return res
            