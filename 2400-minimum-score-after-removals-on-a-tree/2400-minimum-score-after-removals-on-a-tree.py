class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        sub_score = nums[:]
        tin = [0]*len(nums)
        tout = [0]*len(nums)
        time = 0
        def dfs(i,p):
            nonlocal time
            time += 1
            tin[i] = time
            for ne in adj[i]:
                if ne != p:
                    dfs(ne, i)
                    sub_score[i] ^= sub_score[ne]
            tout[i] = time
        def checkInSubtree(u, root):
            return tin[root] <= tin[u] <= tout[root]
        dfs(0, -1)
        res = inf
        for i in range(len(edges)):
            a1,a2 = edges[i]
            if checkInSubtree(a1, a2):
                a1,a2 = a2,a1
            for j in range(i):
                b1,b2 = edges[j]
                if checkInSubtree(b1,b2):
                    b1,b2 = b2,b1

                if checkInSubtree(a2,b2):
                    A = [sub_score[a2],
                        sub_score[b2] ^ sub_score[a2],
                        sub_score[0] ^ sub_score[b2]]
                elif checkInSubtree(b2,a2):
                    A = [sub_score[b2],
                        sub_score[a2] ^ sub_score[b2],
                        sub_score[0] ^ sub_score[a2]]
                else:
                    A = [sub_score[a2],
                        sub_score[b2],
                        sub_score[0] ^ sub_score[a2] ^ sub_score[b2]]
                A.sort()
                res = min(res, A[-1] - A[0])
        return res