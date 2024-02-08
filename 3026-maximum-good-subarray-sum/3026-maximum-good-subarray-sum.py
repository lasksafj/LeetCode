class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        L = {}
        sum_left = 0
        sum_cur = 0
        res = -inf
        for i,x in enumerate(nums):
            sum_cur += x
            if x-k in L:
                res = max(res, sum_cur - L[x-k])
            if x+k in L:
                res = max(res, sum_cur - L[x+k])
            if x not in L or L[x] > sum_left:
                L[x] = sum_left
            sum_left += x
        return res if res > -inf else 0