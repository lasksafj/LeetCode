class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        N = len(s)
        m = defaultdict(lambda:defaultdict(int))
        l = 1
        for i in range(1, k+1):
            if (i*i) % k == 0:
                l = i*2
                break
        # l*l % k == 0, let d = l*l, d%k == 0 => 4d,9d,16d,... %k == 0 => l,2l,3l,... valid length of substring
        m[0][0] = 1
        diff = 0
        res = 0
        for i in range(N):
            diff += 1 if s[i] in 'ueoai' else -1
            # count number of subarray end at i
            res += m[diff][(i+1)%l]
            m[diff][(i+1)%l] += 1
            
        return res