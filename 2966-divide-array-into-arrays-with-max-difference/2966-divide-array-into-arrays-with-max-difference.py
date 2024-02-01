class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        res = []
        i = 0
        while i < len(nums):
            A = [nums[i]]
            j = i+1
            while j < i+3:
                A.append(nums[j])
                j += 1
            if A[-1]-A[0] > k:
                return []
            res.append(A)
            i = j
        return res