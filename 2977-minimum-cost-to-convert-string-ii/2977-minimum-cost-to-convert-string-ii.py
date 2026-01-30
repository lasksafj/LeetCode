class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        unique_strs = set(original) | set(changed)
        id = {s: i for i, s in enumerate(unique_strs)}
        size = len(unique_strs)
        mp = [[inf] * size for _ in range(size)]
        for i in range(size):
            mp[i][i] = 0
        for a,b,c in zip(original, changed, cost):
            u, v = id[a], id[b]
            mp[u][v] = min(mp[u][v], c)
        for k in range(size):
            for u in range(size):
                if mp[u][k] == inf: continue
                for v in range(size):
                    if mp[k][v] == inf: continue
                    mp[u][v] = min(mp[u][v], mp[u][k] + mp[k][v])
                    
        Tsource = {}
        Ttarget = {}
        for A,B in zip(original, changed):
            t = Tsource
            for a in A:
                if a not in t:
                    t[a] = {}
                t = t[a]
            t['#'] = id[A]
            t = Ttarget
            for b in B:
                if b not in t:
                    t[b] = {}
                t = t[b]
            t['#'] = id[B]
        dp = [inf] * (len(target) + 1)
        dp[-1] = 0
        for i in range(len(target)-1, -1, -1):
            if source[i] == target[i]:
                dp[i] = dp[i+1]
            t1 = Tsource
            t2 = Ttarget
            for j in range(i, len(target)):
                c1 = source[j]
                c2 = target[j]
                if c1 not in t1 or c2 not in t2:
                    break
                t1 = t1[c1]
                t2 = t2[c2]
                if '#' in t1 and '#' in t2:
                    id1 = t1['#']
                    id2 = t2['#']
                    dp[i] = min(dp[i], dp[j+1] + mp[id1][id2])
        return dp[0] if dp[0] < inf else -1