class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        adj = [defaultdict(int) for _ in range(n+1)]
        for a,b in edges:
            adj[a][b] = 1
            adj[b][a] = 1
        oddv = [i for i in range(n+1) if len(adj[i]) % 2]
        if len(oddv)%2 or len(oddv) > 4:
            return False
        if len(oddv) == 0:
            return True
        if len(oddv) == 2:
            a,b = oddv
            if adj[a][b] == 0:
                return True
            else:
                for v in range(1,n+1):
                    if adj[v][a] == 0 and adj[v][b] == 0:
                        return True
                return False
        a,b,c,d = oddv
        return adj[a][b] == 0 and adj[c][d] == 0 or \
                adj[a][c] == 0 and adj[b][d] == 0 or \
                adj[a][d] == 0 and adj[b][c] == 0
    