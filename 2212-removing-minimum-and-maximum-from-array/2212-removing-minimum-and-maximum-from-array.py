class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        N = len(nums)
        a,b = nums.index(min(nums)), nums.index(max(nums))
        if a > b:
            a,b = b,a
        return min(b+1, N-a, a+N-b+1)