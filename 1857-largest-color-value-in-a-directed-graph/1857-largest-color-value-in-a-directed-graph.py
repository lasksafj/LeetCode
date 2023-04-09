class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
        path = [False]*len(colors)
        @cache
        def dfs(cur):
            path[cur] = True
            count = defaultdict(int)
            for ne in adj[cur]:
                if path[ne]:
                    return None
                a = dfs(ne)
                if a == None:
                    return None
                for c in string.ascii_lowercase:
                    count[c] = max(count[c], a[c])
            path[cur] = False
            count[colors[cur]] += 1
            return count
        res = 0
        for i in range(len(colors)):
            a = dfs(i)
            if a == None:
                return -1
            res = max(res, max([a[v] for v in a]))
        return res