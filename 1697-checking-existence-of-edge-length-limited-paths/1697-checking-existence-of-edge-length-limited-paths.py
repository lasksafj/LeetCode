class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        f = list(range(n))
        rank = [0]*n
        
        def root(x):
            if x == f[x]:
                return x
            return root(f[x])
        def union(a,b):
            a,b = root(a),root(b)
            if a == b:
                return
            if rank[a] > rank[b]:
                f[b] = a
            elif rank[a] < rank[b]:
                f[a] = b
            else:
                f[b] = a
                rank[a] += 1
        
        edgeList.sort(key=lambda x: x[2])
        queries = sorted([[q[0],q[1],q[2],i] for i,q in enumerate(queries)], key=lambda x: x[2])
        i = 0
        res = [False]*len(queries)
        for a,b,d,j in queries:
            while i < len(edgeList) and edgeList[i][2] < d:
                union(edgeList[i][0], edgeList[i][1])
                i += 1
            if i == len(edgeList) or root(a) == root(b):
                res[j] = True
                
        return res