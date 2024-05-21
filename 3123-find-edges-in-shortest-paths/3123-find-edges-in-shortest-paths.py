def F(adj,start,n):
    res = [inf]*n
    res[start] = 0
    pq = [[0,start]]
    while pq:
        d,cur = heappop(pq)
        if res[cur] < d:
            continue
        for ne,w,_ in adj[cur]:
            if res[ne] > d+w:
                res[ne] = d+w
                heappush(pq, [d+w,ne])
    return res
    
class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        for i,(a,b,w) in enumerate(edges):
            adj[a].append([b,w,i])
            adj[b].append([a,w,i])
        dist1 = F(adj,0,n)
        dist2 = F(adj,n-1,n)
        mi = dist1[n-1]
        
        # print(mi)
        # print(dist1)
        # print(dist2)
        
        res = [False]*len(edges)
        if mi == inf:
            return res
        
        
        for i,(a,b,w) in enumerate(edges):
            if dist1[a] + w + dist2[b] == mi or dist1[b] + w + dist2[a] == mi:
                res[i] = True
        return res