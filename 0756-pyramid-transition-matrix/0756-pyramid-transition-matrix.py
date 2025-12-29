class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        mp = defaultdict(list)
        for a,b,c in allowed:
            mp[a,b].append(c)
        N = len(bottom)
        def dfs(i, j, A):
            if i == N:
                return True
            if i+j == N:
                return dfs(i+1, 0, A + [''])
            for c in mp[A[i-1][j], A[i-1][j+1]]:
                A[-1] += c
                if dfs(i, j+1, A):
                    return True
                A[-1] = A[-1][:-1]
            return False
        return dfs(1, 0, [bottom, ''])