class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m,n = len(board),len(board[0])
        q = deque()
        vis = set()
        for i in range(m):
            if board[i][0] == 'O':
                q.append([i,0])
                vis.add((i,0))
                board[i][0] = '-'
            if board[i][n-1] == 'O':
                q.append([i,n-1])
                vis.add((i,n-1))
                board[i][n-1] = '-'
        for j in range(1,n-1):
            if board[0][j] == 'O':
                q.append([0,j])
                vis.add((0,j))
                board[0][j] = '-'
            if board[m-1][j] == 'O':
                q.append([m-1,j])
                vis.add((m-1,j))
                board[m-1][j] = '-'
        while q:
            x,y = q.popleft()
            for nx,ny in [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]:
                if nx>=0 and ny>=0 and nx<m and ny<n and (nx,ny) not in vis and board[nx][ny] == 'O':
                    q.append([nx,ny])
                    vis.add((nx,ny))
                    board[nx][ny] = '-'
        for i in range(m):
            for j in range(n):
                if board[i][j] == '-':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
                