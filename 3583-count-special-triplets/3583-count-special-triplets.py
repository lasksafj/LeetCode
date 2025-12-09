class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        R = Counter(nums[2:])
        L = Counter([nums[0]])
        res = 0
        for i in range(1, len(nums)-1):
            res += L[nums[i]*2] * R[nums[i]*2]
            L[nums[i]] += 1
            R[nums[i+1]] -= 1
        return res%(10**9+7)