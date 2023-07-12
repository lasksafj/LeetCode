class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        vis = set()
        @cache
        def dfs(cur):
            if cur in vis:
                return False
            vis.add(cur)
            for ne in graph[cur]:
                if dfs(ne) == False:
                    return False
            return True
        res = []
        for cur in range(len(graph)):
            if dfs(cur):
                res.append(cur)
        return res