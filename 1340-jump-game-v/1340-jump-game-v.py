class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        N = len(arr)
        adj = defaultdict(list)
        for i in range(N):
            for j in range(i-1, max(0,i-d)-1, -1):
                if arr[j] >= arr[i]: break
                adj[i].append(j)
            for j in range(i+1, min(N-1,i+d)+1):
                if arr[j] >= arr[i]: break
                adj[i].append(j)
        @cache
        def dfs(i):
            res = 1
            for j in adj[i]:
                res = max(res, dfs(j)+1)
            return res
        return max(dfs(i) for i in range(N))