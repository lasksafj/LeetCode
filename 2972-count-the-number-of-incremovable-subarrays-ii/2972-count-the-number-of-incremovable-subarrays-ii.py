class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        N = len(nums)
        l,rr = N,-1
        for i in range(N-1):
            if nums[i+1] <= nums[i]:
                l = i+1
                break
        for i in range(N-1,0,-1):
            if nums[i-1] >= nums[i]:
                rr = i
                break
        if l == N:
            return (N+1)*N//2
        
        r = rr
        while r < N and nums[r] <= nums[l-1]:
            r += 1
        res = 0
        nums.append(inf)
        for i in range(l,-1,-1):
            a = nums[i-1] if i>0 else 0
            while r >= rr and a < nums[r]:
                r -= 1
            res += N-r
        return res
            