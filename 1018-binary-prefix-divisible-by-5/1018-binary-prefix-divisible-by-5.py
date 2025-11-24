class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        a = 0
        res = []
        for d in nums:
            a = a<<1 | d
            res.append(a%5 == 0)
        return res