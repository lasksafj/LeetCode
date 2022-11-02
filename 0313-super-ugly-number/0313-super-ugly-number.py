class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        primes_len = len(primes)
        num = [0] * primes_len
        dp = [0] * n
        dp[0] = 1
        for i in range(1, n):
            dp[i] = min(dp[num[a]] * primes[a] for a in range(primes_len))
            for a in range(primes_len):
                if dp[i] == dp[num[a]] * primes[a]:
                    num[a] += 1
        return dp[n-1]