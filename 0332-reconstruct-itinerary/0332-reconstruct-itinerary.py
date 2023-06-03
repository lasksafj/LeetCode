class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(deque)
        for a,b in sorted(tickets):
            adj[a].append(b)
        n = len(tickets)
        res = ['JFK']
        def dfs(cur):
            if len(res) == len(tickets)+1:
                return True
            for ne in adj[cur].copy():
                res.append(ne)
                adj[cur].popleft()
                if dfs(ne):
                    return True
                res.pop()
                adj[cur].append(ne)
            return False
        dfs('JFK')
        return res