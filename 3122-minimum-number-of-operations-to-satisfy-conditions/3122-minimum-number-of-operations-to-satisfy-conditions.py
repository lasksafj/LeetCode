class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        M,N = len(grid),len(grid[0])
        cnt = [defaultdict(int) for _ in range(N)]
        for j in range(N):
            for i in range(M):
                cnt[j][grid[i][j]] += 1
        dp = [0]*10
        for j in range(N):
            ndp = [inf]*10
            for i in range(10):
                mi = inf
                for pi in range(10):
                    if i == pi:
                        continue
                    mi = min(mi, dp[pi])
                    ndp[i] = mi + M-cnt[j][i]
            dp = ndp
        return min(dp)