class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        prev = nums[0]-k
        res = 1
        for n in nums[1:]:
            if prev < n+k:
                prev = max(prev+1, n-k)
                res += 1
        return res