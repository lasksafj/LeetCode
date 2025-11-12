class Solution:
    def minOperations(self, nums: List[int]) -> int:
        N = len(nums)
        if 1 in nums: return N-nums.count(1)
        res = inf
        for i in range(N):
            a = nums[i]
            for j in range(i+1, N):
                a = gcd(a, nums[j])
                if a == 1:
                    res = min(res, j-i + N-1)
                    break
        return res if res < inf else -1