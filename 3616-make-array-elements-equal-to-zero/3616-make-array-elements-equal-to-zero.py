class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        r = sum(nums)
        l = 0
        res = 0
        for n in nums:
            if n > 0:
                l += n
                r -= n
            else:
                if l == r:
                    res += 2
                elif abs(l-r) == 1:
                    res += 1
        return res