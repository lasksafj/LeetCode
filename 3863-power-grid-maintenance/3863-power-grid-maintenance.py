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
        off = [inf]*(c+1)
        mp = defaultdict(lambda:inf)
        for i,(t,x) in enumerate(queries):
            if t == 2 and off[x] == inf:
                off[x] = i
        for x in range(1,c+1):
            if off[x] == inf:
                rx = root(x)
                mp[rx] = min(mp[rx], x)
        res = []
        for i in range(len(queries)-1,-1,-1):
            t,x = queries[i]
            if t == 1:
                if off[x] < i:
                    rx = root(x)
                    res.append(mp[rx] if mp[rx] < inf else -1)
                else:
                    res.append(x)
            elif off[x] == i:
                rx = root(x)
                mp[rx] = min(mp[rx], x)
        return res[::-1]