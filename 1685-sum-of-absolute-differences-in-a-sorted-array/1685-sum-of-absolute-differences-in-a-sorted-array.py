class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        s = sum(nums)
        res = []
        a = 0
        N = len(nums)
        for i,n in enumerate(nums):
            b = s-a-n
            res.append( n*i-a + b-(n*(N-i-1)) )
            a += n
        return res