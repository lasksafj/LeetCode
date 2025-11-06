class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for a,b in connections:
            adj[a].append(b)
            adj[b].append(a)
        vis = set()
        cur = set()
        def dfs(i):
            cur.add(i)
            for ne in adj[i]:
                if ne not in cur:
                    dfs(ne)
        mp = {}
        p = [0]*(c+1)
        for i in range(1,c+1):
            if i not in vis:
                cur = set()
                dfs(i)
                vis |= cur
                cur = SortedList(list(cur))
                for j in cur:
                    p[j] = cur[0]
                mp[cur[0]] = cur
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