class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        res = 0
        for i,n in enumerate(nums):
            a = bisect_left(nums, lower-n)
            b = bisect_right(nums, upper-n)
            if a <= i < b:
                res += b-a-1
            else:
                res += b-a
        return res//2