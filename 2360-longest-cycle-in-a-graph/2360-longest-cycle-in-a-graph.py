class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        t = [-1]*len(edges)
        res = [-1]
        vis = set()
        def dfs(cur, i):
            if cur == -1:
                return
            if t[cur] > -1:
                res[0] = max(res[0], i-t[cur])
            else:
                if cur not in vis:
                    vis.add(cur)
                    t[cur] = i
                    dfs(edges[cur], i+1)
                    t[cur] = -1
        for c in range(len(edges)):
            if c not in vis:
                dfs(c, 0)
        return res[0]