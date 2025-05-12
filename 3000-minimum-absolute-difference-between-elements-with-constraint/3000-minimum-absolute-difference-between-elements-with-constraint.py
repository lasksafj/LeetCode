class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        N = len(nums)
        A = SortedList()
        res = inf
        for i in range(x, N):
            A.add(nums[i-x])
            n = nums[i]
            j = A.bisect_right(n)
            if j < len(A):
                res = min(res, A[j] - n)
            if j > 0:
                res = min(res, n - A[j-1])
        return res