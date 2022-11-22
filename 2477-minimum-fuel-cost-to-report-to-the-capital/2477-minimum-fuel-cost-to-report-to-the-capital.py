class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        adj = [[] for _ in range(len(roads)+1)]
        for e in roads:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])
        # print(adj)
        def dfs(cur, prev):
            fuel,nopas = 0,0
            for ne in adj[cur]:
                if ne != prev:
                    a, b = dfs(ne, cur)
                    fuel += a + (b//seats+1 if b%seats else b//seats)
                    nopas += b
            # print(cur, fuel, nopas+1)
            return fuel, nopas+1
        res, _ = dfs(0, -1)
        return res