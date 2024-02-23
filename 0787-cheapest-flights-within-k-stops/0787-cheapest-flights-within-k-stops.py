class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for a,b,p in flights:
            adj[a].append([b,p])
        price = [inf] * n
        price[src] = 0
        q = deque([[0,src]])
        while q and k > -1:
            for _ in range(len(q)):
                p,cur = q.popleft()
                for ne,np in adj[cur]:
                    if price[ne] > p+np:
                        price[ne] = p+np
                        q.append([p+np, ne])
            k -= 1

        return price[dst] if price[dst] != inf else -1
                
                