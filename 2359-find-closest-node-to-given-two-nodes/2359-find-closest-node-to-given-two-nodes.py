class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        m = [[-1]*2 for _ in range(n)]
        m[node1][0] = 0
        m[node2][1] = 0
        i = 0
        while (edges[node1] != -1 and m[edges[node1]][0] == -1) \
            or (edges[node2] != -1 and m[edges[node2]][1] == -1):
            i += 1
            if edges[node1] != -1 and m[edges[node1]][0] == -1:
                node1 = edges[node1]
                m[node1][0] = i
            if edges[node2] != -1 and m[edges[node2]][1] == -1:
                node2 = edges[node2]
                m[node2][1] = i
        res = -1
        dist = inf
        for i in range(n):
            if m[i][0] > -1 and m[i][1] > -1:
                a = max(m[i][0], m[i][1])
                if dist > a:
                    res = i
                    dist = a
        return res
        
         