class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        N = len(nums)
        ma = max(nums)
        j = 0
        d = 0
        res = 0
        for i in range(N):
            d += nums[i] == ma
            while d >= k:
                d -= nums[j] == ma
                j += 1
            res += i-j+1
        # print(res)
        return N*(N+1)//2 - res