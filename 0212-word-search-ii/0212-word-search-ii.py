class Trie:
    def __init__(self):
        self.next = {}
        self.eow = False
        self.cnt = 0

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def add_word(root, w):
            cur = root
            for c in w:
                if c not in cur.next:
                    cur.next[c] = Trie()
                cur = cur.next[c]
                cur.cnt += 1
            cur.eow = True
            
        def remove_word(root, w):
            cur = root
            for c in w:
                cur = cur.next[c]
                cur.cnt -= 1
        
        root = Trie()
        for w in words:
            add_word(root, w)
        
        m,n = len(board), len(board[0])
        vis = [[0]*n for _ in range(m)]
        
        l = [len(words)]
        def dfs(i, j, cur_word, cur):
            if i < 0 or j < 0 or i >= m or j >= n \
                or vis[i][j] or len(cur_word) > 10 or l[0] == 0:
                return
            vis[i][j] = 1

            if board[i][j] in cur.next and cur.next[board[i][j]].cnt > 0:
                cur_word = ''.join((cur_word, board[i][j]))
                cur = cur.next[board[i][j]]
                if cur.eow:
                    res.append(cur_word)
                    cur.eow = False
                    remove_word(root, cur_word)
                    l[0] -= 1
                
                dfs(i+1, j, cur_word, cur)
                dfs(i-1, j, cur_word, cur)
                dfs(i, j+1, cur_word, cur)
                dfs(i, j-1, cur_word, cur)
                
            vis[i][j] = 0
        
        res = []
        for i in range(m):
            for j in range(n):
                dfs(i, j, '', root)
        return res