class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        ma = 0
        A = []
        for n in nums:
            ma = max(ma, n)
            A.append(ma)
        A = sorted([gcd(n,a) for n,a in zip(nums, A)])
        res = 0
        i,j = 0,len(A)-1
        while i < j:
            res += gcd(A[i], A[j])
            i += 1
            j -= 1
        return res