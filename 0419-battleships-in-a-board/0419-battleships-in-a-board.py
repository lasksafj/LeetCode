class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        res = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X' and (i==0 or (i>0 and board[i-1][j] == '.')) and (j==0 or (j>0 and board[i][j-1] == '.')):
                    res += 1
        return res