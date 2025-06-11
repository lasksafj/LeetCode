def z_func(s):
    n = len(s)
    z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i < r:
            z[i] = min(r - i, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l = i
            r = i + z[i]
    return z
class Solution:
    def countCells(self, grid: List[List[str]], pattern: str) -> int:
        M,N = len(grid),len(grid[0])
        fh = lambda k: (k//N, k%N)
        fv = lambda k: (k%M, k//M)
        h = ['']*(M*N)
        v = ['']*(M*N)
        for i in range(M):
            for j in range(N):
                k = i*N+j
                h[k] = grid[i][j]
                k = j*M+i
                v[k] = grid[i][j]
        plen = len(pattern)
        mp = defaultdict(int)
        def sol(Z, f):
            j = plen+1
            for i,v in enumerate(Z):
                if i > plen and v == plen:
                    j = max(j, i)
                    while j < i+plen:
                        mp[f(j-plen-1)] += 1
                        j += 1
        Z = z_func(list(pattern) + ['#'] + h)
        sol(Z, fh)
        Z = z_func(list(pattern) + ['#'] + v)
        sol(Z, fv)
        return len([k for k in mp if mp[k] >= 2])
            