class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        def count(A):
            res = 0
            s = 0
            for i in range(10):
                res += A[i]*s
                s += A[i]
            return res
        mod = 1
        res = 0
        while mod < nums[0]*10:
            A = [0]*10
            for n in nums:
                A[n//mod%10] += 1
            res += count(A)
            mod *= 10
        return res