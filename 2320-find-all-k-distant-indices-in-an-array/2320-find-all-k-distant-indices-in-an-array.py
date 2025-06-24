class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        N = len(nums)
        res = []
        mp = defaultdict(int)
        l,r = 0,0
        for i in range(N):
            while r < N and r-i <= k:
                mp[nums[r]] += 1
                r += 1
            while i-l > k:
                mp[nums[l]] -= 1
                l += 1
            if mp[key]:
                res.append(i)
        return res