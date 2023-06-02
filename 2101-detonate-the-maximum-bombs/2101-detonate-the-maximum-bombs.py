class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        adj = defaultdict(list)
        for i in range(len(bombs)):
            a,b,c = bombs[i]
            for j in range(len(bombs)):
                if j == i:
                    continue
                x,y,_ = bombs[j]
                if (x-a)*(x-a) + (y-b)*(y-b) <= c*c:
                    adj[i].append(j)
        def dfs(cur, vis):
            res = 1
            vis.add(cur)
            for ne in adj[cur]:
                if ne not in vis:
                    res += dfs(ne, vis)
            return res
        res = 0
        for i in range(len(bombs)):
            vis = set()
            res = max(res, dfs(i, vis))
        return res