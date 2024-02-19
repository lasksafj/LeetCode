class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        N = len(nums)
        if N < 2:
            return 0
        @cache
        def go(i, j, x):
            ans = 0
            if i + 1 < j and nums[i] + nums[i+1] == x:
                tmp = go(i+2, j, x) + x
                if tmp > ans:
                    ans = tmp
            if j - 1 > i and nums[j] + nums[j-1] == x:
                tmp = go(i, j-2, x) + x
                if tmp > ans:
                    ans = tmp
            if i < j and nums[i] + nums[j] == x:
                tmp = go(i+1, j-1, x) + x
                if tmp > ans:
                    ans = tmp
            return ans
        even = (go(1, N-2, nums[0] + nums[N-1]) + nums[0] + nums[N-1])//(nums[0] + nums[N-1])
        left = (go(2, N-1, nums[0] + nums[1]) + nums[0] + nums[1])//(nums[0] + nums[1])
        right = (go(0, N-3, nums[-1] + nums[-2]) + nums[-1] + nums[-2])//(nums[-1] + nums[-2])
        return max(even, left, right)