class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        pre = [0]*numCourses
        ind = [0]*numCourses
        for a,b in prerequisites:
            adj[a].append(b)
            ind[b] += 1
        q = deque()
        for a in range(numCourses):
            if ind[a] == 0:
                q.append(a)
        while q:
            a = q.popleft()
            for ne in adj[a]:
                pre[ne] |= 1<<a | pre[a]
                ind[ne] -= 1
                if ind[ne] == 0:
                    q.append(ne)
        res = []
        for a,b in queries:
            res.append(pre[b] & (1<<a) > 0)
        return res