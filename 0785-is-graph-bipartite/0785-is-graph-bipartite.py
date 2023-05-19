class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        m = {}
        for i in range(len(graph)):
            if i not in m:
                q = deque([i])
                m[i] = 1
                while q:
                    c = q.popleft()
                    for ne in graph[c]:
                        if ne not in m:
                            m[ne] = m[c]*-1
                            q.append(ne)
                        elif m[ne] == m[c]:
                            return False
        return True