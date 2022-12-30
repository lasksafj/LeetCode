class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        res = []
        path = []
        def dfs(cur, n):
            path.append(cur)
            if cur == n-1:
                res.append(path[:])
                path.pop()
                return
            for ne in graph[cur]:
                dfs(ne, n)
            path.pop()
        dfs(0, n)
        return res