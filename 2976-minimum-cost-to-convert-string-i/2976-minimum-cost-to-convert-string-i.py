class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        adj = defaultdict(list)
        for a,b,c in zip(original,changed,cost):
            adj[a].append([b,c])
        mp = defaultdict(lambda:defaultdict(lambda:inf))
        for start in set(original):
            mp[start][start] = 0
            q = [[0,start]]
            while q:
                d,cur = heappop(q)
                if mp[start][cur] < d:
                    continue
                for ne,w in adj[cur]:
                    if mp[start][ne] > w+d:
                        mp[start][ne] = w+d
                        heappush(q, [w+d,ne])
        res = 0
        for i in range(len(source)):
            if source[i] != target[i]:
                if source[i] not in mp or target[i] not in mp[source[i]]:
                    return -1
                res += mp[source[i]][target[i]]
        return res