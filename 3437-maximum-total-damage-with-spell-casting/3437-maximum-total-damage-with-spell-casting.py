class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        mp = Counter(power)
        A = sorted(mp.items())
        N = len(A)
        print(A)
        @cache
        def dfs(i):
            if i >= N:
                return 0
            res = dfs(i+1)
            j = i+1
            if j < N and A[j][0] <= A[i][0]+2:
                j += 1
            if j < N and A[j][0] <= A[i][0]+2:
                j += 1
            
            return max(res, dfs(j) + A[i][0]*A[i][1])
        return dfs(0)