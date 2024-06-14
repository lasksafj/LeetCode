class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        N = len(nums)
        def count(A):
            res = 0
            for n in A:
                res += (n>0)
            return res
        def calc_or(A, n):
            i = 0
            while n > 0:
                A[i] += n&1
                n >>= 1
                i += 1
        def calc_deOr(A, n):
            i = 0
            B = A[:]
            while n > 0:
                B[i] -= n&1
                n >>= 1
                i += 1
            return B
        
        res = [0]*N
        j = N-1
        A = [0]*32
        for i in range(N-1,-1,-1):
            calc_or(A, nums[i])
            while i < j:
                B = calc_deOr(A, nums[j])
                if count(B) < count(A):
                    break
                A = B
                j -= 1
            res[i] = j-i+1
        return res
