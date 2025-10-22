class SparseVector:
    def __init__(self, nums: List[int]):
        self.A = []
        for i,n in enumerate(nums):
            if n != 0:
                self.A.append([i,n])

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        i,j = 0,0
        A = self.A
        B = vec.A
        res = 0
        while i < len(A) and j < len(B):
            if A[i][0] == B[j][0]:
                res += A[i][1] * B[j][1]
                i += 1
                j += 1
            elif A[i][0] < B[j][0]:
                i += 1
            else:
                j += 1
        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)