class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        f = list(range(c+1))
        r = [0]*(c+1)
        def root(x):
            while x != f[x]:
                x = f[x]
            return x
        def union(a,b):
            a,b = root(a),root(b)
            if a == b:
                return
            if r[a] < r[b]:
                a,b = b,a
            f[b] = a
            if r[a] == r[b]:
                r[a] += 1

        for a,b in connections:
            union(a,b)
        mp = defaultdict(lambda:SortedList())
        p = [0]*(c+1)
        for i in range(1,c+1):
            p[i] = root(i)
            mp[p[i]].add(i)
        res = []
        off = set()
        for t,x in queries:
            if t == 1:
                if x in off:
                    res.append(mp[p[x]][0] if mp[p[x]] else -1)
                else:
                    res.append(x)
            else:
                mp[p[x]].discard(x)
                off.add(x)
        return res