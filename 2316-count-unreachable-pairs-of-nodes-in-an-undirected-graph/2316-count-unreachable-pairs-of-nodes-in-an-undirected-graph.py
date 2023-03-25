class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        vis = set()
        def dfs(cur):
            ans = 1
            for ne in adj[cur]:
                if ne not in vis:
                    vis.add(ne)
                    ans += dfs(ne)
            return ans
        res = 0
        s = 0
        for i in range(n):
            if i not in vis:
                vis.add(i)
                a = dfs(i)
                res += s*a
                s += a
        return res