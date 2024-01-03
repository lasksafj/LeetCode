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
        
        
        
        dp = [inf]*(len(source)+1)
        dp[0] = 0
        for i in range(1,len(source)+1):
            if source[i-1] == target[i-1]:
                dp[i] = dp[i-1]
                
            for u in list(mp.keys()):
                l = len(u)
                if i-l >= 0 and source[i-l:i] in mp and target[i-l:i] in mp[source[i-l:i]]:
                    dp[i] = min(dp[i], dp[i-l] + mp[source[i-l:i]][target[i-l:i]])
                    
        return dp[-1] if dp[-1] < inf else -1