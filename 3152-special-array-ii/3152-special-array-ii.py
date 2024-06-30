class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        prev = nums[0]&1
        A = []
        for i,n in enumerate(nums):
            n = n&1
            if n != prev:
                prev = n
            else:
                A.append(i)
        res = []
        for a,b in queries:
            res.append(bisect_right(A,a) == bisect_right(A,b))
        return res