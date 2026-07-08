class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9+7
        n = len(s)
        cnt = [0] * (n + 1)
        A = []
        for i,n in enumerate(s):
            cnt[i+1] = cnt[i]
            if n != '0':
                cnt[i+1] += 1
                A.append(int(n))
        m = len(A)
        if m == 0: return [0]*len(queries)

        pref_sum = [0] * (m + 1)
        pref_num = [0] * (m + 1)
        pow10 = [1] * (m + 1)
        for i in range(m):
            pref_sum[i+1] = pref_sum[i] + A[i]
            pref_num[i+1] = (pref_num[i] * 10 + A[i]) % MOD
            pow10[i+1] = (pow10[i] * 10) % MOD

        res = []
        for l,r in queries:
            lA, rA = cnt[l],cnt[r+1]-1
            if lA > rA:
                res.append(0)
                continue
            s1,s2 = pref_sum[lA], pref_sum[rA+1]
            n1,n2 = pref_num[lA], pref_num[rA+1]
            ans = (n2 - n1 * pow10[rA-lA+1]) * (s2-s1) % MOD
            res.append(ans)
        return res