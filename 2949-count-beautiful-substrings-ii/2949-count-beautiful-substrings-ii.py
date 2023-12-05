class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        N = len(s)
        m = defaultdict(lambda:defaultdict(int))
        l = 1
        for i in range(1, k+1):
            if (i*i) % k == 0:
                l = i*2
                break
        m[0][l-1] = 1
        diff = 0
        res = 0
        for i in range(N):
            diff += 1 if s[i] in 'ueoai' else -1
            res += m[diff][i%l]
            m[diff][i%l] += 1
            
        return res