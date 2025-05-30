class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        N = len(edges)
        def bfs(i):
            res = [inf]*N
            step = 0
            q = deque([i])
            vis = {i}
            while q:
                for _ in range(len(q)):
                    i = q.popleft()
                    res[i] = step
                    ne = edges[i]
                    if ne == -1: continue
                    if ne not in vis:
                        vis.add(ne)
                        q.append(ne)
                step += 1
            return res
        A = bfs(node1)
        B = bfs(node2)
        res = [inf, inf]
        for i in range(N):
            res = min(res, [max(A[i], B[i]), i])
        return res[1] if res[0] < inf else -1