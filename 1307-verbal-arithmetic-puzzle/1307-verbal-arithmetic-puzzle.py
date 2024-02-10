class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        words = [w[::-1] for w in words]
        result = result[::-1]
        A = words + [result]
        max_col = max([len(w) for w in A])
        mp = {}
        vis = [0]*10
        def dfs(r,c,bal):
            if c == max_col:
                return bal == 0
            if r == len(A):
                if bal % 10 > 0:
                    return False
                return dfs(0,c+1,bal//10)
            if len(A[r]) > 1 and c == len(A[r])-1 and A[r][c] in mp and mp[A[r][c]] == 0:
                return False
            if c < len(A[r]):
                if A[r][c] not in mp:
                    for d in range(10):
                        if (len(A[r]) > 1 and c == len(A[r])-1 and d == 0) or vis[d]:
                            continue
                        mp[A[r][c]] = d
                        vis[d] = 1
                        if dfs(r+1,c, bal+d if r < len(words) else bal-d):
                            return True
                        del mp[A[r][c]]
                        vis[d] = 0
                    return False
                else:
                    n = mp[A[r][c]]
                    return dfs(r+1,c, bal+n if r < len(words) else bal-n)
            else:
                return dfs(r+1,c,bal)
                
        return dfs(0,0,0)
