class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        # Split a cell in to 4 parts.
        # We give it a number top is 0, left is 1, bottom is 2, right is 3.

        n = len(grid)
        f = {}
        r = defaultdict(int)
        def root(x):
            if x not in f:
                f[x] = x
            if x == f[x]:
                return x
            return root(f[x])
        def union(a,b):
            a,b = root(a),root(b)
            if a == b:
                return 
            if r[a] < r[b]:
                f[a] = b
            elif r[a] > r[b]:
                f[b] = a
            else:
                f[a] = b
                r[b] += 1
        
        for i in range(n):
            for j in range(n):
                if i:
                    union((i,j,0), (i-1,j,2))
                if j:
                    union((i,j,1), (i,j-1,3))
                if grid[i][j] == '/':
                    union((i,j,0), (i,j,1))
                    union((i,j,2), (i,j,3))
                elif grid[i][j] == '\\':
                    union((i,j,0), (i,j,3))
                    union((i,j,1), (i,j,2))
                else:
                    union((i,j,0), (i,j,1))
                    union((i,j,1), (i,j,2))
                    union((i,j,2), (i,j,3))
        return len(set(root(x) for x in f))