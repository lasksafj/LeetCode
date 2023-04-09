class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
        path = [False]*len(colors)
        vis = [False]*len(colors)
        count = [defaultdict(int) for _ in range(len(colors))]
        path = [False]*len(colors)
        def dfs(cur):
            if path[cur]:
                return inf
            if vis[cur]:
                return count[cur][colors[cur]]
            path[cur] = True
            vis[cur] = True
            for ne in adj[cur]:
                if dfs(ne) == inf:
                    return inf
                for c in string.ascii_lowercase:
                    count[cur][c] = max(count[cur][c], count[ne][c])
            path[cur] = False
            count[cur][colors[cur]] += 1
            return count[cur][colors[cur]]
        res = 0
        for i in range(len(colors)):
            res = max(res, dfs(i))
        return res if res < inf else -1