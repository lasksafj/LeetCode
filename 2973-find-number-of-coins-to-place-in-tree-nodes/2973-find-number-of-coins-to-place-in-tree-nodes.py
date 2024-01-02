class Solution:
    def placedCoins(self, edges: List[List[int]], cost: List[int]) -> List[int]:
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        res = [0]*len(cost)
        def dfs(i,prev):
            a,b,c = cost[i],-inf,-inf
            d,e = cost[i],inf
            for ne in adj[i]:
                if ne != prev:
                    na,nb,nc,nd,ne = dfs(ne,i)
                    a,b,c = sorted([a,b,c,na,nb,nc], reverse=True)[:3]
                    d,e = sorted([d,e,nd,ne])[:2]
            val = 1
            if c > -inf:
                val = max(a*b*c, 0)
                if e < inf:
                    val = max(val, d*e*a)
            res[i] = val if -inf < val < inf else 1
            # print(i,'---',a,b,c,d,e)
            return (a,b,c,d,e)
        
        dfs(0,-1)
        return res