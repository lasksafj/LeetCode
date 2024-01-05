class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        A = [nums[0]]
        for n in nums[1:]:
            if n > A[-1]:
                A.append(n)
            else:
                p = bisect_left(A, n)
                A[p] = n
            
        return len(A)