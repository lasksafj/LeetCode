class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        N = len(strs[0])
        dp = [1]*N
        for i in range(N-2,-1,-1):
            for j in range(i+1,N):
                if all(strs[r][i] <= strs[r][j] for r in range(len(strs))):
                    dp[i] = max(dp[i], dp[j] + 1)
        return N - max(dp)