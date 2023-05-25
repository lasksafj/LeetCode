class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        n = len(specialRoads)
        edges = []
        for a,b,c,d,e in specialRoads:
            if abs(c-a)+abs(d-b) > e:
                edges.append([a,b,c,d,e])
        vis = defaultdict(int)
        vis[(target[0],target[1])] = abs(target[0]-start[0])+abs(target[1]-start[1])
        for a,b,c,d,e in edges:
            vis[(c,d)] = abs(c-start[0])+abs(d-start[1])
        
        pq = [(0,start[0],start[1])]
        while pq:
            cost,x,y = heappop(pq)
            for a,b,c,d,e in edges:
                if x!=c or y!=d:
                    w = min(abs(a-x)+abs(b-y)+e, abs(c-x)+abs(d-y))
                    if cost+w < vis[(c,d)]:
                        heappush(pq, (cost+w, c,d))
                        vis[(c,d)] = cost+w
        res = vis[(target[0],target[1])]
        for a,b,c,d,e in edges:
            res = min(res, vis[(c,d)] + abs(target[0]-c)+abs(target[1]-d))
        return res