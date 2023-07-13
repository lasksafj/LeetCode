class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for a,b in prerequisites:
            adj[b].append(a)
        vis = set()
        @cache
        def dfs(cur):
            if cur in vis:
                return False
            vis.add(cur)
            for ne in adj[cur]:
                if not dfs(ne):
                    return False
            return True
        for i in range(numCourses):
            if dfs(i) == False:
                return False
        return True