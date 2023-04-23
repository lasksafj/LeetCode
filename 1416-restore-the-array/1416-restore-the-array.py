class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1
        lenk = 0
        kk = k
        while kk > 0:
            lenk += 1
            kk //= 10
        for i in range(n):
            j = i
            b = lenk
            while j >= 0 and b > 0:
                a = int(s[j:i+1])
                if a > k:
                    break
                if s[j] != '0':
                    dp[i+1] += dp[j]
                j -= 1
                b -= 1
        return dp[n] % 1000000007
                