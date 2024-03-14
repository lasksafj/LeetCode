class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def sol(k):
            j = 0
            s = 0
            res = 0
            for i in range(len(nums)):
                s += nums[i]
                while j <= i and s > k:
                    s -= nums[j]
                    j += 1
                res += i-j+1
            return res
        return sol(goal) - sol(goal-1)