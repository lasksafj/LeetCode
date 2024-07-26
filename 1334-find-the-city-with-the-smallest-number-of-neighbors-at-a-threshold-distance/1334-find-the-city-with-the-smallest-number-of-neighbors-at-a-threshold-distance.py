class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[inf]*n for _ in range(n)]
        for a,b,w in edges:
            dist[a][b] = w
            dist[b][a] = w
        for i in range(n):
            dist[i][i] = 0
        
        for k in range(n):
            for a in range(n):
                for b in range(n):
                    dist[a][b] = min(dist[a][b], dist[a][k] + dist[k][b])
        
        res = 0
        ma = inf
        for a in range(n):
            cnt = -1
            for b in range(n):
                if dist[a][b] <= distanceThreshold:
                    cnt += 1
            if cnt <= ma:
                res = a
                ma = cnt
        return res