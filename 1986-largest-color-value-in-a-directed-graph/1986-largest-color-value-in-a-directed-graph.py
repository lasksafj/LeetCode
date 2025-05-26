class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        N = len(colors)
        colors = [ord(c)-97 for c in colors]
        adj = defaultdict(list)
        ind = [0]*N
        for a,b in edges:
            adj[a].append(b)
            ind[b] += 1
        q = deque()
        dp = [[0]*26 for _ in range(N)]
        for i in range(N):
            if ind[i] == 0:
                q.append(i)
                dp[i][colors[i]] = 1
        res = 0
        n = 0
        while q:
            for _ in range(len(q)):
                i = q.popleft()
                n += 1
                for ne in adj[i]:
                    for c in range(26):
                        dp[ne][c] = max(dp[ne][c], dp[i][c])
                    ind[ne] -= 1
                    if ind[ne] == 0:
                        q.append(ne)
                        dp[ne][colors[ne]] += 1
        return max(max(r) for r in dp) if n == N else -1