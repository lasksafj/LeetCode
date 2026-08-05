class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        invoked = defaultdict(set)
        for a,b in invocations:
            adj[a].append(b)
            invoked[b].add(a)
            
        def bfs(i, res):
            q = deque([i])
            res.add(i)
            while q:
                i = q.popleft()
                for ne in adj[i]:
                    if ne not in res:
                        res.add(ne)
                        q.append(ne)
            
        suspicious = set()
        bfs(k, suspicious)
        for i in suspicious:
            for invoker in invoked[i]:
                if invoker not in suspicious:
                    return list(range(n))
        return list(set(range(n)) - suspicious)