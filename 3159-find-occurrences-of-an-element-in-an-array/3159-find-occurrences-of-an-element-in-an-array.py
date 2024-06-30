class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        A = []
        for i,n in enumerate(nums):
            if n == x:
                A.append(i)
        res = []
        for q in queries:
            res.append(A[q-1] if q <= len(A) else -1)
        return res