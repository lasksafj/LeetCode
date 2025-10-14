class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        res = [0]*len(nums)
        l = 0
        prev = inf
        for i,n in enumerate(nums):
            if n > prev:
                l += 1
            else:
                l = 1
            prev = n
            if l >= k:
                res[i] = 1
        for i in range(len(nums)-k):
            if res[i] & res[i+k]:
                return True
        return False