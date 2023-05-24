class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        nums.sort()
        a = 0
        prev = nums[0]
        res = nums[0]*nums[0]*nums[0]
        for n in nums[1:]:
            res += (a*2 + prev + n)*n*n
            a = a*2 + prev
            prev = n
        return res % 1000000007