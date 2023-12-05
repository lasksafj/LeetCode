class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        N = len(s)
        m = defaultdict(lambda:defaultdict(int))
        m[0][0] = 1
        res = 0
        a,b = 0,0
        for i in range(N):
            if s[i] in 'euoai':
                a += 1
            else:
                b += 1
            for j in m[a-b]:
                if (a-j)*(a-j) % k == 0:
                    res += m[a-b][j]
            m[a-b][a%k] += 1
            
        return res