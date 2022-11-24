class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n = len(board),len(board[0])
        def dfs(i,j,cur):
            if i < 0 or j < 0 or i == m or j == n or cur == len(word) or board[i][j] != word[cur]:
                return False
            if cur == len(word)-1 and board[i][j] == word[cur]:
                return True
            c = board[i][j]
            board[i][j] = '.'
            res = 0
            if dfs(i+1,j, cur+1):
                res = True
            elif dfs(i-1,j, cur+1):
                res = True
            elif dfs(i,j+1, cur+1):
                res = True
            elif dfs(i,j-1, cur+1):
                res = True
            board[i][j] = c
            return res
        
        cnt = Counter(word)
        if cnt[word[0]] > cnt[word[-1]]:
            word = word[::-1]
        for i in range(m):
            for j in range(n):
                if dfs(i,j,0):
                    return True
        return False
            
            
            