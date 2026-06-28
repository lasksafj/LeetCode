class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        a = 0
        for n in sorted(arr):
            if n-a > 1:
                a += 1
            else:
                a = n
        return a