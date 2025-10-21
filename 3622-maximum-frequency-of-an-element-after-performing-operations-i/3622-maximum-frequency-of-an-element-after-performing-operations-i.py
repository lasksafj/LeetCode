class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        # case 1: change to nums[i]
        # case 2: change to n != every nums[i]
        nums.sort()
        N = len(nums)
        cnt = Counter(nums)
        res = 0
        l,r = 0,0
        for i,n in enumerate(nums):
            while nums[l] < n-k: l += 1
            while r < N and nums[r] <= n+k: r += 1
            res = max(res, min(numOperations, r-l-cnt[n]) + cnt[n])
        if res > numOperations: return res
        j = 0
        for i,n in enumerate(nums):
            while n-2*k > nums[j]:
                j += 1
            res = max(res, min(numOperations, i-j+1))
        return res