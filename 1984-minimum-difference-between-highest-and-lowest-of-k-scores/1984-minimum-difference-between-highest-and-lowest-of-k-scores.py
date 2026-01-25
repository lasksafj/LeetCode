class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        A = sorted(nums)
        res = inf
        for i in range(k-1, len(A)):
            res = min(res, A[i] - A[i-k+1])
        return res