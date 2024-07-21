class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topo(edges):
            adj = defaultdict(list)
            ind = [0]*(k+1)
            for a,b in edges:
                adj[a].append(b)
                ind[b] += 1
            q = deque([])
            for i in range(1,k+1):
                if ind[i] == 0:
                    q.append(i)
            res = []
            while q:
                for _ in range(len(q)):
                    i = q.popleft()
                    res.append(i)
                    for ne in adj[i]:
                        ind[ne] -= 1
                        if ind[ne] == 0:
                            q.append(ne)
            return res if len(res) == k else []
        
        row = topo(rowConditions)
        col = topo(colConditions)
        if row == [] or col == []:
            return []
        mp = {}
        for j,n in enumerate(col):
            mp[n] = j
        res = [[0]*k for _ in range(k)]
        for i,n in enumerate(row):
            res[i][mp[n]] = n
        return res