class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        components = []
        seen = set()
        for i in range(1, n+1):
            if i in seen:
                continue
            seen.add(i)
            q = deque([i])
            vis = set([i])
            while q:
                a = q.popleft()
                for ne in adj[a]:
                    if ne not in vis:
                        vis.add(ne)
                        q.append(ne)
                        seen.add(ne)
            components.append(vis)
        
        def bfs(node):
            res = 0
            q = deque([node])
            cur_group = set()
            vis = set([node])
            while q:
                res += 1
                group = set()
                for _ in range(len(q)):
                    a = q.popleft()
                    for ne in adj[a]:
                        if ne in cur_group:
                            return -1
                        if ne not in vis:
                            vis.add(ne)
                            q.append(ne)
                            group.add(ne)
                cur_group = group
            return res
        
        max_no_groups = [-1] * len(components)
        for i in range(len(components)):
            for node in components[i]:
                max_no_groups[i] = max(max_no_groups[i], bfs(node))
            if max_no_groups[i] == -1:
                return -1
        return sum(max_no_groups)