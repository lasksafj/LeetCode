class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        def sol(firstLen, secondLen):
            s1 = sum(nums[:firstLen])
            dp1 = s1
            s2 = sum(nums[firstLen:firstLen+secondLen])
            dp2 = s1+s2
            res = dp2
            for i in range(firstLen+secondLen, len(nums)):
                s1 = s1 - nums[i-(firstLen+secondLen)] + nums[i-secondLen]
                dp1 = max(dp1, s1)
                s2 = s2 - nums[i-secondLen] + nums[i]
                dp2 = max(dp2, dp1 + s2)
                res = max(res, dp2)
            return res
        return max(sol(firstLen, secondLen), sol(secondLen, firstLen))