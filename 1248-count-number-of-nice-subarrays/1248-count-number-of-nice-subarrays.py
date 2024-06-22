class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMost(k):
            j = 0
            res = 0
            s = 0
            for i in range(len(nums)):
                s += nums[i]%2
                while s > k:
                    s -= nums[j]%2
                    j += 1
                res += i-j+1
            return res
        return atMost(k) - atMost(k-1)