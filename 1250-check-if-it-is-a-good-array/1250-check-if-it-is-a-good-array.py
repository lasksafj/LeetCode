class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        res = nums[0]
        for n in nums:
            res = gcd(n, res)
            if res == 1:
                return True
        return False