class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        M,N = len(strs),len(strs[0])
        dp = [1]*N
        for i in range(N):
            for j in range(i):
                if all(strs[k][j] <= strs[k][i] for k in range(M)):
                    dp[i] = max(dp[i], dp[j] + 1)
        return N - max(dp)