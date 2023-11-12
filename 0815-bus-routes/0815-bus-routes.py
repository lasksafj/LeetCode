class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        N = len(routes)
        adj = defaultdict(list)
        q = deque()
        stop = set()
        vis = [0]*N
        for i in range(N):
            for j in range(i):
                if set(routes[i]).intersection(routes[j]):
                    adj[i].append(j)
                    adj[j].append(i)
            if source in set(routes[i]):
                q.append(i)
                vis[i] = 1
            if target in set(routes[i]):
                stop.add(i)

        res = 1
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur in stop:
                    return res
                for ne in adj[cur]:
                    if vis[ne] == 0:
                        vis[ne] = 1
                        q.append(ne)
            res += 1
        return -1