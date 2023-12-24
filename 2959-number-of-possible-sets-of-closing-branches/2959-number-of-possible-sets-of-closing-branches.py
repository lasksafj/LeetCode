class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        def f(adj,start,V):
            dist = [inf]*n
            q = [[0,start]]
            dist[start] = 0
            while q:
                d,v = heappop(q)
                if dist[v] > d:
                    continue
                for ne,w in adj[v]:
                    if w+d < dist[ne]:
                        dist[ne] = w+d
                        heappush(q, [w+d,ne])
            # print('dist',dist)
            for v in V:
                if maxDistance < dist[v]:
                    return False
            return True
            
        res = 0
        for i in range(2**n):
            A = [[a,b,c] for a,b,c in roads if ((1<<a)&i > 0) and ((1<<b)&i > 0)]
            V = [v for v in range(n) if (1<<v)&i > 0]
            adj = defaultdict(list)
            for a,b,c in A:
                adj[a].append((b,c))
                adj[b].append((a,c))
            ok = True
            # print(A, adj)
            for start in V:
                if f(adj,start,V) == False:
                    ok = False
                    break
            if ok:
                # print(i)
                res += 1
        return res