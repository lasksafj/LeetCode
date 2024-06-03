class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        N = len(nums)
        mp = {}
        cur = 0
        for i in range(N):
            cur += nums[i]
            if (cur%k == 0 and i>0) or cur%k in mp and mp[cur%k]<i-1:
                return True
            if cur%k not in mp:
                mp[cur%k] = i
        return False