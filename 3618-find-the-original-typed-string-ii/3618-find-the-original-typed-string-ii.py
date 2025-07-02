class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        MOD = 10**9+7
        A = []
        N = len(word)
        i = 0
        res = 1
        while i < N:
            j = i+1
            while j < N and word[j] == word[i]:
                j += 1
            A.append(j-i-1)
            res = (res*(j-i)) % MOD
            i = j
        if k <= len(A):
            return res
        k -= len(A)
        pre = [1]*k
        for i in range(len(A)):
            npre = [0]*k
            npre[0] = 1
            for s in range(1, k):
                # ndp[s] = dp[s] .. dp[s-A[i]]
                # ndp[s] = pref_dp[s+1] - pref_dp[max(0, s-A[i])]
                # npref_dp[s+1] = npref_dp[s] + ndp[s]
                npre[s] = npre[s-1] + pre[s] - (pre[s-A[i]-1] if s-A[i]-1 >= 0 else 0)
            pre = npre
        return (res - pre[-1]) % MOD