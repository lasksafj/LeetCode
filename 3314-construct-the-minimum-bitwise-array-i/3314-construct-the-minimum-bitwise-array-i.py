class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        res = []
        for n in nums:
            if n&1 == 0:
                res.append(-1)
            else:
                a = n+1
                res.append( n&(~((a&(-a)) >> 1)) )
        return res