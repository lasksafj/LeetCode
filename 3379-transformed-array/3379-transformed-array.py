class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = [0]*N
        for i,n in enumerate(nums):
            if n != 0:
                res[i] = nums[(i+n+N)%N]
            else:
                res[i] = n
        return res