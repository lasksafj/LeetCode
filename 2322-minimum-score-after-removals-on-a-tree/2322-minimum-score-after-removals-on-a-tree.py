class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        score = [0]*len(nums)
        f = [set() for _ in range(len(nums))]
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        def dfs(prev, cur):
            res = nums[cur]
            f[cur].update(f[prev])
            f[cur].add(prev)
            for ne in adj[cur]:
                if ne != prev:
                    res ^= dfs(cur, ne)
            score[cur] = res
            return res
        s = dfs(-1,0)
        # print(s)
        res = inf
        for i in range(len(edges)):
            for j in range(i):
                a,b = edges[i]
                v1 = b if a in f[b] else a
                a,b = edges[j]
                v2 = b if a in f[b] else a
                if v2 in f[v1]:
                    v1,v2 = v2,v1
                if v1 in f[v2]:
                    s2 = score[v2]
                    s1 = s ^ score[v1]
                    s3 = s ^ s1 ^ s2
                else:
                    s1 = score[v1]
                    s2 = score[v2]
                    s3 = s ^ s1 ^ s2
                # print(edges[i], edges[j], s1,s2,s3, v1 in f[v2], v1, v2)
                res = min(res, max(s1,s2,s3) - min(s1,s2,s3))
        return res
            