class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        A = [x for x in nums if x>=0]
        B = [x for x in nums if x<0]
        res = []
        i = 0
        while i < len(A):
            res.append(A[i])
            if i < len(B):
                res.append(B[i])
            i += 1
        return res + B[i:]