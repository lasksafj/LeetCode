fact = [1]*5001
for i in range(1,len(fact)):
    fact[i] = fact[i-1] * i

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        cnt = Counter(s)
        center = ''
        mp = {}
        for c,v in cnt.items():
            mp[c] = v//2
            if v&1:
                center = c
        A = sorted([c,v] for c,v in mp.items())
        n = sum(mp.values())
        p = fact[n]
        for c,v in A:
            p //= fact[v]
        if k > p:
            return ''
        res = ''
        while n:
            for i,(c,v) in enumerate(A):
                if k <= (p * v//n):
                    res += c
                    A[i][1] -= 1
                    p = p * v//n
                    break
                k -= p * v//n
            n -= 1

        return res + center + res[::-1]
