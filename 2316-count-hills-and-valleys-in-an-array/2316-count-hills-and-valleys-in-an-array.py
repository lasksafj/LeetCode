class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        i = 0
        res = 0
        N = len(nums)
        while i < N:
            j = i+1
            while j < N and nums[j]==nums[i]:
                j += 1
            if (i and nums[i-1] < nums[i]) and (j<N and nums[i] > nums[j]) or\
                (i and nums[i-1] > nums[i]) and (j<N and nums[i] < nums[j]):
                res += 1
            i = j
        return res