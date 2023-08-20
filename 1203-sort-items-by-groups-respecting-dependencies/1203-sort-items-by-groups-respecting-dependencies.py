class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        def topo(adj, deg):
            q = deque([i for i in range(len(deg)) if deg[i] == 0])
            res = []
            while q:
                for _ in range(len(q)):
                    cur = q.popleft()
                    res.append(cur)
                    for ne in adj[cur]:
                        deg[ne] -= 1
                        if deg[ne] == 0:
                            q.append(ne)
            return res if len(res) == len(adj) else []
        
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1
        adj_group = [[] for _ in range(m)]
        adj_item = [[] for _ in range(n)]
        deg_group = [0]*m
        deg_item = [0]*n
        for i in range(n):
            for j in beforeItems[i]:
                if group[j] != group[i]:
                    adj_group[group[j]].append(group[i])
                    deg_group[group[i]] += 1
                adj_item[j].append(i)
                deg_item[i] += 1
        group_order = topo(adj_group, deg_group)
        item_order = topo(adj_item, deg_item)
        if not group_order or not item_order:
            return []
        mp = defaultdict(list)
        res = []
        for i in item_order:
            mp[group[i]].append(i)
        for i in group_order:
            res += mp[i]
        return res
    