class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        j = 0
        s = 0
        cur = 0
        for i,n in enumerate(nums):
            s += n
            cur = s*(i-j+1)
            while j <= i and cur >= k:
                s -= nums[j]
                j += 1
                cur = s*(i-j+1)
            res += i-j+1
        return res