class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        def dfs(prev, cur, time, p):
            if cur == target and time == 0:
                return p
            if time < 0:
                return 0
            L = len(adj[cur])
            if prev in adj[cur]:
                L -= 1
            if L == 0:
                if cur == target:
                    return p
                return 0
            p /= L
            res = 0
            for ne in adj[cur]:
                if ne != prev:
                    res = max(res, dfs(cur, ne, time-1, p))
            return res
            
        return dfs(0,1,t,1)