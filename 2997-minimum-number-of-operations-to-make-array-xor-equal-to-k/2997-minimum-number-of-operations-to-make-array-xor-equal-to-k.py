class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        A = [0]*32
        for n in nums:
            i = 0
            while n > 0:
                A[i] += n&1
                n >>= 1
                i += 1
        res = 0
        for i in range(32):
            if k&1:
                res += A[i]&1 == 0
            else:
                res += A[i]&1 == 1
            k >>= 1
        return res