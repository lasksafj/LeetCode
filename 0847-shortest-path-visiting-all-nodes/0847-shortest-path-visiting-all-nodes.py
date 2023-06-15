class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        q = deque()
        vis = set()
        for i in range(n):
            q.append((i, 1<<i))
        res = 0
        while q:
            for _ in range(len(q)):
                node, mask = q.popleft()
                if mask == (1<<n)-1:
                    return res
                for ne in graph[node]:
                    nmask = mask|(1<<ne)
                    if (ne, nmask) not in vis:
                        q.append((ne, nmask))
                        vis.add((ne, nmask))
            res += 1
        return -1