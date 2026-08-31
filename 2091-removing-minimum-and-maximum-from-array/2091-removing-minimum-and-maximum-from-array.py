class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        N = len(nums)
        mi,ma = min(nums),max(nums)
        i,j = nums.index(mi), nums.index(ma)
        if i > j: i,j = j,i
        return min(j+1, N-i, i+1 + N-j)