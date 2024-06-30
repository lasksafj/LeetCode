class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        prev = nums[0]&1
        A = [0]*(len(nums)+1)
        for i,n in enumerate(nums):
            n = n&1
            A[i+1] = A[i] + (n==prev)
            prev = n
        res = []
        for a,b in queries:
            res.append(A[a+1] == A[b+1])
        return res