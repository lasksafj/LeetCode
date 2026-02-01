class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        a,b = inf,inf
        for n in nums[1:]:
            if n < a:
                b = a
                a = n
            elif n < b:
                b = n
        return nums[0] + a + b