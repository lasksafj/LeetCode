class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        edges = []
        for a,b,c,d,e in specialRoads:
            if abs(c-a)+abs(d-b) > e:
                edges.append([a,b,c,d,e])
        edges.append([target[0],target[1],target[0],target[1],0])
        vis = defaultdict(int)
        vis[(target[0],target[1])] = inf
        for a,b,c,d,e in edges:
            vis[(c,d)] = inf
        
        pq = [(0, *start)]
        while pq:
            cost,x,y = heappop(pq)
            if [x,y] == target:
                return cost
            for a,b,c,d,e in edges:
                if x!=c or y!=d:
                    w = abs(a-x)+abs(b-y)+e
                    if cost+w < vis[(c,d)]:
                        heappush(pq, (cost+w, c,d))
                        vis[(c,d)] = cost+w
        return -1