class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        p = [i for i in range(n)]
        r = [0]*n
        def root(x):
            if x != p[x]:
                return root(p[x])
            return x
        def union(a,b):
            if r[a] > r[b]:
                p[b] = a
            elif r[a] < r[b]:
                p[a] = b
            else:
                p[b] = a
                r[a] += 1
        rem_con = 0
        for a,b in connections:
            ra,rb = root(a),root(b)
            if ra != rb:
                union(ra,rb)
            else:
                rem_con += 1
        p = [root(i) for i in range(n)]
        nogroup = len(Counter(p))-1
        if nogroup > rem_con:
            return -1
        return nogroup
        