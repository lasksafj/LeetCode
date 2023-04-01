class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        adj = defaultdict(set)
        for a,b in edges:
            adj[a].add(b)
            adj[b].add(a)
        q,q2 = deque(), deque()
        for e in adj:
            if len(adj[e]) == 1:
                if coins[e] == 0:
                    q.append(e)
                else:
                    q2.append(e)
        # print(q)
        while q:
            a = q.popleft()
            while len(adj[a]) == 1 and coins[a] == 0:
                b = list(adj[a])[0]
                adj[b].remove(a)
                del adj[a]
                a = b
            if len(adj[a]) == 1:
                q2.append(a)
        # print(q2)
        for _ in range(2):
            for _ in range(len(q2)):
                a = q2.popleft()
                if len(adj[a]) > 0:
                    b = list(adj[a])[0]
                    adj[b].remove(a)
                    if len(adj[b]) == 1:
                        q2.append(b)
                del adj[a]
        # print(adj)
        res = (len(adj)-1)*2
        return res if res > 0 else 0
            