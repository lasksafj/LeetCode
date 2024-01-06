def has_cycle(adj):
    vis = [0]*61
    def dfs(i):
        vis[i] = 1
        for ne in adj[i]:
            if vis[ne] == 2:
                continue
            if vis[ne] == 1:
                return True
            if dfs(ne):
                return True
        vis[i] = 2
        return False
    for i in range(1,61):
        if vis[i] == 0 and dfs(i):
            return True
    return False

class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        M,N = len(targetGrid),len(targetGrid[0])
        mp = [[N-1,0,M-1,0] for _ in range(61)] # left,right,top,bottom for each color
        for i in range(M):
            for j in range(N):
                d = targetGrid[i][j]
                mp[d][0] = min(mp[d][0], j)
                mp[d][1] = max(mp[d][1], j)
                mp[d][2] = min(mp[d][2], i)
                mp[d][3] = max(mp[d][3], i)
        adj = defaultdict(set)
        for d in range(1,61):
            for i in range(mp[d][2], mp[d][3]+1):
                for j in range(mp[d][0], mp[d][1]+1):
                    if targetGrid[i][j] != d:
                        adj[d].add(targetGrid[i][j])
        return not has_cycle(adj)