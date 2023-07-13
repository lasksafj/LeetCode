class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indeg = [0]*numCourses
        adj = defaultdict(list)
        for a,b in prerequisites:
            indeg[a] += 1
            adj[b].append(a)
        q = deque()
        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)
        res = []
        while q:
            cur = q.popleft()
            res.append(cur)
            for ne in adj[cur]:
                indeg[ne] -= 1
                if indeg[ne] == 0:
                    q.append(ne)
        return res if len(res) == numCourses else []