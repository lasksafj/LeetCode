class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        def dfs_bob(prev, cur, time):
            if cur == 0:
                bob_time[cur] = time
                return 1
            res = 0
            for ne in adj[cur]:
                if ne != prev:
                    res |= dfs_bob(cur, ne, time+1)
            if res:
                bob_time[cur] = time
                return 1
            return 0
        
        n = len(amount)
        adj = [[] for _ in range(n)]
        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])
        bob_time = [inf] * n
        dfs_bob(-1, bob, 0)
        
        # print(bob_time)
        
        @cache
        def dfs_alice(prev, cur, time):
            cost = 0
            if time < bob_time[cur]:
                cost = amount[cur]
            elif time == bob_time[cur]:
                cost = amount[cur]//2
                
            res = -inf
            leaf = 1
            for ne in adj[cur]:
                if ne != prev:
                    leaf = 0
                    res = max(res, dfs_alice(cur, ne, time+1))
            # print(cur, cost, res, )
            return cost if leaf else cost + res
        
        return dfs_alice(-1, 0, 0)