class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
#         l^2/4 = x*k => l = 2*sqrt(x*k)
        l = 1
        for i in range(1,k+1):
            a = int(sqrt(i*k))
            if a*a == i*k:
                l = 2*a
                break
                
        mp = defaultdict(lambda:defaultdict(int))
        mp[0][(-1)%l] = 1
        res = 0
        diff = 0
        for i in range(len(s)):
            if s[i] in 'aeiou':
                diff += 1
            else:
                diff -= 1
            res += mp[diff][(i)%l]
            mp[diff][i%l] += 1
        return res