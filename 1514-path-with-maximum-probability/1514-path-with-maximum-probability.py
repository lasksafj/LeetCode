class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj = [[] for _ in range(n)]
        for i,e in enumerate(edges):
            adj[e[0]].append([e[1], succProb[i]])
            adj[e[1]].append([e[0], succProb[i]])
        prob = [0] * n
        prob[start] = 1
        pq = [[-1,start]]
        while pq:
            cur_prob, cur_e = heapq.heappop(pq)
            cur_prob *= -1
            for ne, np in adj[cur_e]:
                if prob[ne] < cur_prob * np:
                    prob[ne] = cur_prob * np
                    heapq.heappush(pq, [-cur_prob * np, ne])
        return prob[end]
        