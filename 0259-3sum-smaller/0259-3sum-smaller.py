class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        N = len(nums)
        res = 0
        for i in range(N):
            j = i+1
            k = N-1
            s = target - nums[i]
            while j < k:
                if nums[j] + nums[k] < s:
                    res += k-j
                    j += 1
                else:
                    k -= 1
        return res