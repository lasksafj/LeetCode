class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        m,n = len(mat),len(mat[0])
        r,c = [0]*m, [0]*n
        p = defaultdict(list)
        for i in range(m):
            for j in range(n):
                p[mat[i][j]].append((i,j))
                
        dp = [[0]*n for _ in range(m)]
        for a in sorted(p):
            for i,j in p[a]:
                dp[i][j] = max(r[i], c[j]) + 1
            for i,j in p[a]:
                r[i] = max(r[i], dp[i][j])
                c[j] = max(c[j], dp[i][j])
        
        return max(max(r),max(c))