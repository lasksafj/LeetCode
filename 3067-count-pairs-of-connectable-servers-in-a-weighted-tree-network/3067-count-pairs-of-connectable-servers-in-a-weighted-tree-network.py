class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        adj = defaultdict(list)
        for a,b,w in edges:
            adj[a].append((b,w))
            adj[b].append((a,w))
        
        dp = [0] * len(adj)
        def sol(start):
            def dfs(i, prev, cur):
                res = 0
                if cur % signalSpeed == 0:
                    res += 1
                for ne,w in adj[i]:
                    if ne != prev:
                        res += dfs(ne, i, cur+w)
                return res
            pre = 0
            res = 0
            for ne_start,w in adj[start]:
                a = dfs(ne_start, start, w)
                res += a*pre
                pre += a
            return res
        return [sol(i) for i in range(len(adj))]