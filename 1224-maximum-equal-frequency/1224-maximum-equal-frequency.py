class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        mi = 0
        ma = 0
        res = 1
        mp = defaultdict(int)
        freq = defaultdict(int)
        for i,n in enumerate(nums):
            a = mp[n]
            mp[n] += 1
            if a in freq:
                freq[a] -= 1
                if freq[a] == 0:
                    del freq[a]
                    if a == mi:
                        mi = a+1
            else:
                mi = 1
            freq[a+1] += 1
            if a == ma:
                ma = a+1
            if (len(freq) == 1 and (ma == 1 or ma == i+1)) or (len(freq) == 2 and ((mi+1 == ma and freq[ma] == 1) or (mi == 1 and freq[mi] == 1))):
                res = max(res, i+1)
        return res