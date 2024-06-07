class Solution:
    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        N = len(nums)
        no_sub = (N+1)*N//2
        
        def check(mi):
            j = 0
            mp = defaultdict(int)
            res = 0
            for i in range(N):
                mp[nums[i]] += 1
                while len(mp) > mi:
                    mp[nums[j]] -= 1
                    if mp[nums[j]] == 0:
                        del mp[nums[j]]
                    j += 1
                res += i-j+1
            return res >= (no_sub+1)//2
        
        l,r = 1,len(nums)
        while l <= r:
            mi = (l+r)//2
            if check(mi):
                r = mi-1
            else:
                l = mi+1
        return l
                