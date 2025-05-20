class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        A = [nums[0]] + [b-a for a,b in pairwise(nums)] + [0]
        for a,b in queries:
            A[a] -= 1
            A[b+1] += 1
        cur = 0
        for a in A[:-1]:
            cur += a
            if cur > 0:
                return False
        return True