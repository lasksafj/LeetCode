class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        R = [set() for _ in range(9)]
        C = [set() for _ in range(9)]
        B = [set() for _ in range(9)]
        def check(i,j,n):
            k = i//3 * 3 + j//3
            if n in R[i] or n in C[j] or n in B[k]:
                return False
            return True
        def add(i,j,n):
            board[i][j] = str(n)
            R[i].add(n)
            C[j].add(n)
            k = i//3 * 3 + j//3
            B[k].add(n)
        def remove(i,j):
            n = board[i][j]
            board[i][j] = '.'
            R[i].remove(n)
            C[j].remove(n)
            k = i//3 * 3 + j//3
            B[k].remove(n)
        def next(cur):
            i,j = cur
            j += 1
            if j == 9:
                i += 1
                j = 0
            return (i,j)
            
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    add(i,j,board[i][j])
        
        def dfs(cur):
            i,j = cur
            if i == 9:
                return True
            if board[i][j] != '.':
                return dfs(next(cur))
            for n in '123456789':
                if check(i,j,n):
                    add(i,j,n)
                    if dfs(next(cur)):
                        return True
                    remove(i,j)
            return False
        dfs((0,0))