class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        if nums[0] >= nums[1]: return False
        cnt = 0
        p = nums[1]
        pp = nums[0]
        for n in nums[2:]:
            if n == p:
                return False
            elif (n-p)*(p-pp) < 0:
                cnt += 1
            pp = p
            p = n
        return cnt == 2