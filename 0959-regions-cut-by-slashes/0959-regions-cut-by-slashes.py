class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)+1
        
        f = list(range(n*n))
        r = [0]*(n*n)
        def root(x):
            if x == f[x]:
                return x
            return root(f[x])
        def union(a,b):
            a,b = root(a),root(b)
            if a == b:
                return 1
            if r[a] < r[b]:
                f[a] = b
            elif r[a] > r[b]:
                f[b] = a
            else:
                f[a] = b
                r[b] += 1
            return 0
        
        for i in range(n):
            for j in range(n):
                if i==0 or i==n-1 or j==0 or j==n-1:
                    d = i*n+j
                    union(d, 0)
        res = 1
        for i in range(n-1):
            for j in range(n-1):
                if grid[i][j] == '/':
                    d1 = i*n+j+1
                    d2 = (i+1)*n+j
                    res += union(d1, d2)
                elif grid[i][j] == '\\':
                    d1 = i*n+j
                    d2 = (i+1)*n+j+1
                    res += union(d1, d2)
        return res