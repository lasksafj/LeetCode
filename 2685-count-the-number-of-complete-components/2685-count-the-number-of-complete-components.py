class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        vis = set()
        def bfs(i):
            # print(i)
            vis.add(i)
            v_cnt, e_cnt = 0,0
            q = deque([i])
            while q:
                # print(q)
                v_cnt += len(q)
                for _ in range(len(q)):
                    i = q.popleft()
                    for ne in adj[i]:
                        if ne not in vis:
                            vis.add(ne)
                            q.append(ne)
                        e_cnt += 1
            # print(v_cnt, e_cnt)
            return v_cnt, e_cnt//2
                  
        res = 0
        for i in range(n):
            if i not in vis:
                v_cnt, e_cnt = bfs(i)
                if v_cnt*(v_cnt-1)//2 == e_cnt:
                    res += 1
        return res