class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        m = [-1] * (n*n+1)
        
        d = 1
        k = -n
        for i in range(n-1,-1,-1):
            if d == 1:
                k += n+1
            else:
                k += n-1
            for j in range(n):
                m[k] = board[i][j]
                k += d
            d *= -1
        dist = [-1] * (n*n+1)
        q = deque([1])
        dist[1] = 0
        while q:
            cur = q.popleft()
            for ne in range(cur+1, min(cur+6, n*n)+1):
                if m[ne] != -1:
                    ne = m[ne]
                if dist[ne] == -1:
                    dist[ne] = dist[cur]+1
                    q.append(ne)
        return dist[n*n]