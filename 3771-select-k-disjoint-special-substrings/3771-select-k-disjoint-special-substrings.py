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
            ok = True
            l,r = first[ch], last[ch]
            i = l+1
            while i <= r:
                if first[s[i]] < l:
                    ok = False
                    break
                r = max(r, last[s[i]])
                i += 1
            if ok and (l > 0 or r < N-1):
                A.append([l,r])
        A.sort()
        res = 0
        last_r = -1
        for l,r in A:
            if l > last_r:
                res += 1
                last_r = r
            else:
                last_r = min(last_r, r)
        return res >= k