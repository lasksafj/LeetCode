class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        N = len(nums)
        A = nums+nums
        s =  sum(nums)
        cur = 0
        for i in range(N):
            cur += A[i]*i
        res = cur
        j = 0
        for i in range(N, 2*N):
            cur += A[i]*i - A[j]*j - s
            # print(i,cur,s)
            res = max(res, cur)
            j += 1
        return res