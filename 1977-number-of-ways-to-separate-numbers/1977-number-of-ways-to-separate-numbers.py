class Solution:
    def numberOfCombinations(self, num: str) -> int:
        if num[0] == '0':
            return 0
        if len(num) == 1:
            return 1
        N = len(num)
        mod = 10**9+7
        
        lcp = [[0]*(N) for _ in range(N)]
        for i in range(N-1,-1,-1):
            for j in range(N-1,-1,-1):
                if num[i] == num[j]:
                    lcp[i][j] = (lcp[i+1][j+1] if i+1 < N and j+1 < N else 0) + 1
        
        def gte(a1,a2,b1):
            c = lcp[a1][b1]
            if a1+c >= a2:
                return True
            return num[a1+c] >= num[b1+c]

        
        dp = [[0]*N for _ in range(N)]
        ans = 0
        for i in range(N-1,-1,-1):
            for j in range(i,-1,-1):
                res = 0
                if i+1 == N:
                    res = 1
                else:
                    res = dp[j][i+1]
                if num[i] == '0':
                    dp[j][i] = res
                    continue
                k = i+i-j
                if k > N:
                    dp[j][i] = res
                    continue
                elif k-i > 0 and gte(i,k,j):
                    if k == N:
                        res += 1
                    else:
                        res = (res + dp[i][k]) % mod
                else:
                    if k+1 == N:
                        res += 1
                    elif k+1 < N:
                        res = (res + dp[i][k+1]) % mod
                dp[j][i] = res % mod
            ans = dp[0][1]
            del dp[i]
        return ans % mod