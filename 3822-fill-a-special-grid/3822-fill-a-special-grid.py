class Solution:
    def specialGrid(self, n: int) -> List[List[int]]:
        d = 0
        res = [[0]*2**n for _ in range(2**n)]
        def dfs(i,j,size):
            nonlocal d            
            if size == 1:
                res[i][j] = d
                d += 1
                return
            k = size//2
            dfs(i,j,k)
            dfs(i+k,j,k)
            dfs(i+k,j-k,k)
            dfs(i,j-k,k)
        dfs(0, 2**n-1, 2**n)
        return res