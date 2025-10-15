class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        N = len(nums)
        def f(A, d):
            l = 0
            prev = 0
            res = [1]*N
            for i,n in enumerate(A):
                if (n-prev)*d > 0:
                    l += 1
                else:
                    l = 1
                prev = n
                res[i] = l
            return res
        L = f(nums,1)
        R = f(nums[::-1],-1)[::-1]
        return max(min(a,b) for a,b in zip(L,R[1:]))