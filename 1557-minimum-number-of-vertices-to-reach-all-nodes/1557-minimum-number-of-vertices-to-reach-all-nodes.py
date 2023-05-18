class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        res,vis = set(),set()
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
        for i in range(n):
            if i not in vis:
                res.add(i)
                vis.add(i)
                q = deque([i])
                while q:
                    c = q.popleft()
                    for ne in adj[c]:
                        if ne not in vis:
                            q.append(ne)
                            vis.add(ne)
                        else:
                            if ne in res:
                                res.remove(ne)
        return res