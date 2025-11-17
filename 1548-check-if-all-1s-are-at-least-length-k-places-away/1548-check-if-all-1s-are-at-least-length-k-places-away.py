class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        l = -inf
        for i,n in enumerate(nums):
            if n:
                if i-l-1 < k:
                    return False
                l = i
        return True