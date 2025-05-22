class Solution:
    def maxSubstringLength(self, s: str, k: int) -> bool:
        if k == 0:
            return True
        N = len(s)
        last = {}
        first = {}
        for i in range(N):
            if s[i] not in first:
                first[s[i]] = i
            last[s[i]] = i
        A = []
        for ch in first:
            a,b = first[ch], last[ch]
            ok = True
            i,j = a,b
            while i < j:
                j = max(j, last[s[i]])
                i += 1
            b = j
            i = a
            while j > i:
                i = min(i, first[s[j]])
                j -= 1
            a = i
            if a > 0 or b < N-1:
                A.append([a,b])
        if not A:
            return False
        A.sort(key=lambda x:x[1])
        dp = [1]*len(A)
        for i in range(len(A)):
            a = A[i][0]
            j = bisect_right(A, a-1, key=lambda x:x[1]) - 1
            if j < 0:
                if i:
                    dp[i] = dp[i-1]
            else:
                dp[i] = max(dp[i-1], dp[j] + 1)
        return dp[-1] >= k