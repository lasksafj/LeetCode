class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        for j in range(n):
            a = nums[j]
            for i in range(j, n):
                a = lcm(a, nums[i])
                if a == k:
                    res += 1
                
        return res
                
            